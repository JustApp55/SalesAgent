# Sales Agent Prototype

## Overview
This project is a Streamlit-based prototype for a Sales Assistant Agent powered by OpenAI's GPT models. It helps sales representatives quickly generate actionable insights about prospective accounts, competitors, and company strategy, all in a clean one-page summary.

## Features
- User-friendly Streamlit interface
- Integration with OpenAI GPT (gpt-3.5-turbo)
- Strong prompt engineering for targeted, structured outputs
- Clean, professional one-page output
- Error handling and user feedback

## Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd SalesAgent
```

### 2. Install dependencies
```
pip install streamlit openai python-dotenv watchdog
```

### 3. Set up OpenAI API Key
- Create a `.env` file in the project root:
  ```
  OPENAI_API_KEY=your-api-key-here
  ```
- Get your API key from https://platform.openai.com/api-keys

### 4. Run the app
```
streamlit run app.py
```
- Open your browser to [http://localhost:8501](http://localhost:8501)

## Usage
1. Fill in all required fields in the app.
2. (Optional) Upload a product overview document.
3. Click **Generate Insights**.
4. Review and use the generated one-pager for your sales preparation.

## Customization
- To change the prompt or output structure, edit the `build_prompt()` function in `app.py`.
- To use a different OpenAI model, update the `model` parameter in the code.

## Optional Features & Enhancements
- **Alert System:** Integrate email or Slack notifications for new press releases or job postings.
- **Production Deployment:** Deploy with Streamlit Cloud, Heroku, or Docker for team access.
- **Document Parsing:** Add logic to extract and summarize content from uploaded files.
- **Advanced Prompting:** Experiment with prompt chaining or multi-agent workflows.

## Documentation
- See the `docs/` folder or below for technical write-up, time management, challenges, and experiments.

## License
MIT License

## Production Deployment

### Deploying to Streamlit Cloud
1. Push your project (including `requirements.txt` and `.env` template) to GitHub.
2. Go to https://share.streamlit.io/ and connect your repo.
3. Set your `OPENAI_API_KEY` as a secret in the Streamlit Cloud dashboard.
4. Click Deploy.

### Deploying with Docker
1. Create a `Dockerfile` in your project root:
   ```Dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY . .
   RUN pip install --no-cache-dir -r requirements.txt
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```
2. Build and run:
   ```sh
   docker build -t sales-agent .
   docker run -p 8501:8501 --env OPENAI_API_KEY=your-key-here sales-agent
   ```
