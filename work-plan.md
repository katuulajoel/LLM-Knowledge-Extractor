#### Work Plan

## 1. Project Initialization
**Task:** Set up project structure with FastAPI boilerplate.  

## 2. Basic API Endpoint
**Task:** Add `/analyze` endpoint that accepts text input.  

## 3. Integrate OpenAI (Summary & Topics)
**Task:** Connect OpenAI API and implement logic for:
- 1–2 sentence summary
- Extract title and topics
- Extract sentiment (positive/neutral/negative)  

## 4. Add spaCy for Keyword Extraction
**Task:** Use spaCy POS tagging to get top 3 most frequent nouns.  

## 5. Combine LLM + NLP Results
**Task:** Merge OpenAI results with spaCy keywords into JSON response.  

## 6. Minimal Web UI
**Task:** Add simple HTML form with text input and results display.  

## 7. Styling with Tailwind
**Task:** Add Tailwind CSS for responsive, clean UI.  

## 8. Dockerization
**Task:** Add Dockerfile & docker-compose for easy setup.  

## 9. Setup Script & Environment
**Task:** Add setup script (setup.sh) + .env support.  

## 10. Basic Tests
**Task:** Write pytest test for /analyze endpoint.  

## 11. Polish & Documentation
**Task:** Add README with setup, usage, design choices, trade-offs, and improvements.  