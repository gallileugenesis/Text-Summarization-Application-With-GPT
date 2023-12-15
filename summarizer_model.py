from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summarizer(
    model,
    max_tokens,
    temperature,
    top_p,
    frequency_penalty,
    prompt,
    person_type,
):
    chat = client.chat.completions.create(
        model=model,
        # The upper limit of the generated words by the model
        max_tokens=max_tokens, 
        # The randomness of the model output, with a higher temperature, 
        # means a more diverse and creative result.
        temperature=temperature, 
        # é um parâmetro para controlar o conjunto de amostragem a partir da distribuição 
        # de saída. Por exemplo, o valor 0,1 significa que o modelo apenas amostra a saída
        # dos 10% superiores da distribuição.
        top_p=top_p,
        # A penalidade para o token de repetição da saída. O valor varia entre -2 e 2, 
        # valores positivos impediriam o modelo de repetir o token, 
        # valores negativos encorajariam o modelo a usar palavras mais repetitivas.
        # 0 significa sem penalidade.
        frequency_penalty=frequency_penalty,
        # O parâmetro onde passamos nosso prompt de texto para ser processado com o modelo
        # O papel “sistema” é o conjunto de diretrizes para o modelo de comportamento “assistente”,
        # A função “usuário” representa o prompt da pessoa que interage com o modelo,
        # A função “assistente” é a resposta ao prompt do “usuário”
        messages=
       [
         {
          "role": "system",
          "content": "You are a helpful assistant for text summarization.",
         },
         {
          "role": "user",
          "content": f"Summarize this for a {person_type}: {prompt}",
         },
        ],
    )
    return chat.choices[0].message.content