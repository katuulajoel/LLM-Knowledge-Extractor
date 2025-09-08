# LLM Knowledge Extractor

A FastAPI-based application for extracting and analyzing knowledge from text using LLMs and NLP techniques.

## Features

- Text analysis with OpenAI
- Topic extraction
- Sentiment analysis
- Keyword extraction using spaCy
- RESTful API endpoints
- Modern web interface

## Prerequisites

- Python 3.9+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm-knowledge-extractor.git
   cd llm-knowledge-extractor
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the environment variables in `.env` as needed

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Interactive API docs: [/docs](http://localhost:8000/docs)
- Alternative API docs: [/redoc](http://localhost:8000/redoc)

## Project Structure

```
.
├── app/                    # Application source code
│   ├── __init__.py
│   ├── main.py            # FastAPI application
│   └── config.py          # Application configuration
├── .env                   # Environment variables
├── .gitignore
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## License

MIT
