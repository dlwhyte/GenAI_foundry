# GenAI Foundry — Applied Generative AI Demos
# Build: docker build -t genai-foundry .
# Run:   docker run -p 8501:8501 genai-foundry
# With API key: docker run -p 8501:8501 -e OPENAI_API_KEY=sk-your-key genai-foundry

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY Home.py .
COPY pages/ pages/
COPY estel/ estel/

# Expose Streamlit port
EXPOSE 8501

# Streamlit configuration
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Run the app
CMD ["streamlit", "run", "Home.py"]
