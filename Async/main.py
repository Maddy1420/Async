import os
import asyncio
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()

async def main():
    client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

    prompts = ["Tell me a joke", "What is the capital of India", "What is 2+2"]

    async def ask(prompt):  
        response = await client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    # Use * to unpack the generator into separate arguments for gather
    results = await asyncio.gather(*(ask(p) for p in prompts))
    
    for r in results:
        print(r)
        print("-" * 20)

# Invoke main with parentheses ()
asyncio.run(main())