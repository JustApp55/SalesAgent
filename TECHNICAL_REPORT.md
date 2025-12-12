# Technical Report: Sales Agent Prototype

## 1. Technical Setup
- **Environment:** Python 3.9+
- **Libraries:** Streamlit, OpenAI, python-dotenv, watchdog
- **LLM:** OpenAI GPT (gpt-3.5-turbo)
- **API Key Management:** .env file with python-dotenv
- **UI:** Streamlit app with sidebar instructions and error handling

## 2. Time Management
- **Day 1:**
  - Environment setup and dependency installation
  - Streamlit UI scaffolding
  - OpenAI API integration and testing
- **Day 2:**
  - Prompt engineering and output refinement
  - Error handling and user feedback
  - UI/UX improvements
  - Documentation and optional features

## 3. Challenges and Solutions
- **OpenAI API changes:**
  - Solution: Updated code to use new OpenAI Python API (>=1.0.0)
- **Quota/Access errors:**
  - Solution: Checked billing, switched to gpt-3.5-turbo for broader access
- **Output formatting:**
  - Solution: Used markdown and Streamlit features for clean, readable output

## 4. Experiments
- **Prompt Iterations:**
  - Tried various prompt structures for clarity and relevance
  - Added explicit section headings and bullet points
- **Model Selection:**
  - Compared gpt-4 and gpt-3.5-turbo (used gpt-3.5-turbo for compatibility)
- **Error Handling:**
  - Tested for missing API key, quota exceeded, and invalid input scenarios

## 5. System Outputs
- **One-pager Example:**
  - Company Strategy
  - Competitor Mentions
  - Leadership Information
  - Product/Strategy Summary
  - Article & Source Links

## 6. Optional Enhancements
- Alert system for new press releases or job postings
- Production deployment (Streamlit Cloud, Docker, etc.)
- Advanced document parsing and multi-agent workflows

## 7. References
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

---
*Prepared as part of the Capstone Project: Sales Agent Prototype*
