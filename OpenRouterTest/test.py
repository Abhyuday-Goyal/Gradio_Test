from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPEN_ROUTER_KEY")
)
prompt = input("ask your question:")
completion = client.chat.completions.create(
    extra_headers={},
    model="nousresearch/nous-capybara-7b:free",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
)
print(completion.choices[0].message.content)
