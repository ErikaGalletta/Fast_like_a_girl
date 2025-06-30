from fastapi import FastAPI
from pydantic import BaseModel
from training_ideas import TrainingIdeas  # Your existing Python class
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

class PhaseRequest(BaseModel):
    phase: str
    
app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://192.168.8.182:19006"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/suggest-training/")
def suggest_training(req: PhaseRequest):
    suggestions = TrainingIdeas(req.phase).get_training_idea()
    return suggestions
