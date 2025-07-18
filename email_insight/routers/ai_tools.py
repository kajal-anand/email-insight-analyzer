from fastapi import APIRouter
from email_insight.models.request_models import TextRequest
from email_insight.services import gemini_services

router = APIRouter()

@router.post("/spam-detection")
def spam_detection(request: TextRequest):
    result = gemini_services.detect_spam(request.text)
    return {"result": result}

@router.post("/summarize")
def summarize(request: TextRequest):
    result = gemini_services.summarize_text(request.text)
    return {"summary": result}

@router.post("/ner")
def named_entity_recognition(request: TextRequest):
    result = gemini_services.extract_named_entities(request.text)

    # ✅ Ensure result is a dictionary with "entities" key
    if "error" in result:
        return {"entities": []}
    
    return {"entities": result}

