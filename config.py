import cohere
import os
from app import app

class Config:
    Secret_Key = os.environ.get('SECRET_KEY') or "There is no secret key"
