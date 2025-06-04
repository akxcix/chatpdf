# chatpdf
Chat with your PDFs using local LLMs

A Python application that allows you to interact with your PDF documents using local Language Models. Upload your PDFs and ask questions about their content in a conversational interface.

## Features

- PDF document upload and processing
- Interactive chat interface
- Local LLM integration for privacy
- Streamlit-based web interface
- Support for multiple PDF formats

## Requirements

- Python 3.8 or higher
- uv (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akxcix/chatpdf.git
cd chatpdf
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
```

## Running

1. Make sure your virtual environment is activated
2. Run the application:
```bash
streamlit run src/main.py
```

The application will start and open in your default web browser at `http://localhost:8501`

