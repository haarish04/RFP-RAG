from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

client = Together(api_key =os.getenv("TOGETHER_API_KEY"))

stream = client.chat.completions.create(
  model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
  messages=[
            {"role": "system", "content": "You are an assistant helping me generate mock question and answers"},
            {"role": "user", "content": f"Generate about 20 question and answer pairs. Format the response as question and answer"}],
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=True)