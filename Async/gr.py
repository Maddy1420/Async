import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Retrieve all currently active models on your account
models = client.models.list()

for model in models.data:
    print(model.id)