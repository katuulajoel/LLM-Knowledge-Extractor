from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import os
import spacy
import openai
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize settings and FastAPI app
app = FastAPI(
    title="LLM Knowledge Extractor",
    version="0.1.0",
    description="LLM Knowledge Extractor - Extract and analyze knowledge from text using LLMs"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model for NLP
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # If model not found, download it
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("Warning: OPENAI_API_KEY not found in environment variables")
    client = None
else:
    client = openai.OpenAI(api_key=openai_api_key)

class TextAnalysis(BaseModel):
    text: str

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to LLM Knowledge Extractor!",
        "version": "0.1.0",
        "docs": "/docs"
    }

@app.post("/analyze")
async def analyze_text(analysis: TextAnalysis):
    try:
        # Process text with spaCy for keywords
        doc = nlp(analysis.text)
        
        # Extract nouns for keywords
        nouns = [token.text.lower() for token in doc if token.pos_ == "NOUN"]
        # Get most common nouns
        keywords = [word for word, count in 
                   sorted({word: nouns.count(word) for word in set(nouns)}.items(), 
                         key=lambda item: item[1], 
                         reverse=True)][:3]
        
        # Prepare prompt for OpenAI
        prompt = f"""
        Analyze the following text and provide:
        1. A 1-2 sentence summary
        2. A title (if apparent)
        3. 3 key topics
        4. Sentiment (positive/neutral/negative)
        
        Text: {analysis.text}
        
        Respond in JSON format with these fields: summary, title, topics (list), sentiment
        """
        
        # Call OpenAI API if client is available
        if not client:
            raise HTTPException(status_code=500, detail="OpenAI client not properly initialized. Please check your API key.")
            
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        # Parse the response
        try:
            result = json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            # Fallback in case the response isn't valid JSON
            result = {
                "summary": "Could not generate summary",
                "title": "",
                "topics": [],
                "sentiment": "neutral"
            }
        
        # Add keywords from spaCy
        result["keywords"] = keywords
        
        return {
            "summary": result.get("summary", ""),
            "metadata": {
                "title": result.get("title", ""),
                "topics": result.get("topics", []),
                "sentiment": result.get("sentiment", "neutral"),
                "keywords": keywords
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
