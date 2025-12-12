

import streamlit as st


import openai
import os
from dotenv import load_dotenv
import PyPDF2
import docx
from pptx import Presentation

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


st.set_page_config(page_title="Sales Agent Prototype", layout="centered")
st.title(":bar_chart: Sales Agent Prototype")

# Sidebar for instructions
with st.sidebar:
    st.header("Instructions")
    st.markdown("""
    1. Fill in all required fields.
    2. (Optional) Upload a product overview document.
    3. Click **Generate Insights** to receive a one-page summary.
    4. Review the output and use it for your sales preparation.
    """)

st.write("""
<span style='font-size:18px;'>Enter the details below to generate account insights for your sales opportunity.</span>
""", unsafe_allow_html=True)

# Input fields
product_name = st.text_input("Product Name", help="What product are you selling?")
company_url = st.text_input("Company URL", help="URL of the company you are targeting")
product_category = st.text_input("Product Category", help="E.g., Data Warehousing, Cloud Data Platform")
competitors = st.text_area("Competitors (URLs)", help="Enter one URL per line")
value_proposition = st.text_input("Value Proposition", help="Summarize the product's value in one sentence")
target_customer = st.text_input("Target Customer", help="Name of the person you are trying to sell to")

uploaded_file = st.file_uploader("Optional: Upload a product overview sheet or deck", type=["pdf", "docx", "pptx", "txt"])


def extract_text_from_file(uploaded_file):
    if uploaded_file is None:
        return ""
    if uploaded_file.type == "application/pdf":
        try:
            reader = PyPDF2.PdfReader(uploaded_file)
            text = " ".join(page.extract_text() or "" for page in reader.pages)
            return text[:2000]  # Limit to 2000 chars
        except Exception:
            return "[Could not extract text from PDF]"
    elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        try:
            doc = docx.Document(uploaded_file)
            text = " ".join([p.text for p in doc.paragraphs])
            return text[:2000]
        except Exception:
            return "[Could not extract text from DOCX]"
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.presentationml.presentation":
        try:
            prs = Presentation(uploaded_file)
            text = " ".join([shape.text for slide in prs.slides for shape in slide.shapes if hasattr(shape, "text")])
            return text[:2000]
        except Exception:
            return "[Could not extract text from PPTX]"
    elif uploaded_file.type == "text/plain":
        try:
            return uploaded_file.read().decode("utf-8")[:2000]
        except Exception:
            return "[Could not extract text from TXT]"
    else:
        return "[Unsupported file type]"

def build_prompt():
    doc_text = extract_text_from_file(uploaded_file)
    prompt = f"""
You are a professional sales insights assistant. Using the information below, generate a concise, well-structured one-page summary for a sales representative preparing for a client meeting. Use clear section headings and bullet points where appropriate. Only use information relevant to the sales context.

---
Product Name: {product_name}
Company URL: {company_url}
Product Category: {product_category}
Competitors: {competitors}
Value Proposition: {value_proposition}
Target Customer: {target_customer}
---

Product Overview Document Extract (if provided):
{doc_text}
---

Your output should include the following sections:

1. **Company Strategy**
   - Summarize the company's activities and direction in the relevant industry.
   - Reference any public statements, press releases, or articles by key executives (e.g., Chief Data Officer, Chief Compliance Officer).
   - Mention relevant job postings or technology stack indicators if available.

2. **Competitor Mentions**
   - Note any public information about the listed competitors and their relationship to the target company.

3. **Leadership Information**
   - List key leaders at the prospect company, especially those quoted in recent press releases or articles.

4. **Product/Strategy Summary**
   - For public companies, include insights from annual reports or other relevant documents.

5. **Article & Source Links**
   - Provide links to any referenced articles, press releases, or sources.

Format the output as a clean, readable one-pager. Be concise, factual, and actionable for a sales representative.
"""
    return prompt

if st.button("Generate Insights"):
    if not openai_api_key:
        st.error("OpenAI API key not found. Please set it in your .env file.")
    elif not product_name or not company_url:
        st.warning("Please fill in at least Product Name and Company URL.")
    else:
        with st.spinner("Generating insights with GPT..."):
            try:
                client = openai.OpenAI(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful sales assistant agent."},
                        {"role": "user", "content": build_prompt()}
                    ],
                    max_tokens=800,
                    temperature=0.7
                )
                st.success("Insights generated!")
                # Render output with better formatting
                st.markdown("---")
                st.markdown("<h3>Sales Account Insights</h3>", unsafe_allow_html=True)
                st.markdown(response.choices[0].message.content, unsafe_allow_html=True)
                st.markdown("---")
            except openai.APIStatusError as api_err:
                if api_err.status_code == 429:
                    st.error("You have exceeded your OpenAI API quota or rate limit. Please check your usage and billing details.")
                elif api_err.status_code == 401:
                    st.error("Invalid OpenAI API key. Please check your .env file.")
                else:
                    st.error(f"OpenAI API error: {api_err}")
            except Exception as e:
                st.error(f"Unexpected error generating insights: {e}")
