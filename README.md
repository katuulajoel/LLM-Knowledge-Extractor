# LLM Knowledge Extractor

A simple web application that extracts key information from text using OpenAI's GPT-3.5 and spaCy for natural language processing.

## Features

- Extracts a 1-2 sentence summary from input text
- Identifies key topics and sentiment
- Extracts most frequent nouns as keywords
- Clean, responsive web interface
- Simple REST API endpoint

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- [OpenAI API key](https://platform.openai.com/account/api-keys)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone git@github.com:katuulajoel/LLM-Knowledge-Extractor.git
   cd "LLM Knowledge Extractor"
   ```

2. **Set up environment variables**
   Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Using Docker

1. **Build and run with Docker**
   ```bash
   docker-compose up --build
   ```
   The application will be available at `http://localhost:8000`

### Local Development

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Download spaCy model
   python -m spacy download en_core_web_sm
   
   # Run the application
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://localhost:8000`

2. **Running Tests**
   ```bash
   python -m pytest tests/test_api.py -v
   ```

### API Endpoint

You can also use the API directly:

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "Your text here..."}'
```

## Project Structure

```
.
├── app/
│   ├── static/           # Static files (CSS, JS, images)
│   │   └── styles.css    # Custom styles
│   ├── templates/        # HTML templates
│   │   └── index.html    # Web interface
│   └── main.py          # FastAPI application
├── tests/
│   └── test_api.py      # API tests
├── .env                 # Environment variables
├── .gitignore          # Git ignore file
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── setup.sh           # Setup script
└── README.md          # This file
```

## Design Choices

1. **FastAPI**: Chosen for its performance, automatic request validation, and OpenAPI documentation.
2. **spaCy**: Used for efficient NLP tasks like part-of-speech tagging to extract nouns.
3. **OpenAI GPT-3.5**: Provides high-quality text summarization and metadata extraction.
4. **Tailwind CSS**: Used for rapid UI development with a clean, responsive design.

## Trade-offs

1. **Error Handling**: Basic error handling is implemented, but production use would benefit from more robust error handling and logging.
2. **Rate Limiting**: No rate limiting is implemented, which would be important for a production API.
3. **Model Size**: Using the small spaCy model for speed; larger models might provide better accuracy.
4. **Security**: Input validation is basic; in production, you'd want more robust input sanitization.

## Future Improvements

- Implement rate limiting
- Add support for file uploads (PDF, DOCX, etc.)
- Add more detailed analytics and visualizations
