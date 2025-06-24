from together import Together
from app.config import TOGETHER_API_KEY

def ask_llama(ques : str, context):
    client = Together(api_key =TOGETHER_API_KEY)

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {"role": "system", "content": "You are an assistant helping me with answering user queries. Use only the information provided by me, your main role to is to paraphrase my data. If my ques does not directly match the question in my context, let me know what is the closest question and its answer, paraphrase this"},
            {"role": "user", "content": f"Answer the question: {ques}. Use only the information provided here: {context}"}],
    )

    return response.choices[0].message.content