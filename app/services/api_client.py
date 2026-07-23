import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def envia_prompt(texto):
    # Configura o cliente com chave de API
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
        )

    prompt = f""" 
    Organize uma grade de horários para mim:
    {texto}
    Com as colunas: Dia, Hora, Atividade, Estado.
    dia da semana, segunda...
    Hora nesse formato 10:00-11:00
    E a atividade apenas o nome, do que eu preciso fazer
    No estado coloque apenas False
    Retorne apenas a tabela em formato csv com somenete 
    essas tarefas que pedi para colocar.
    """
    # Faz a requisição ao modelo Gemini mais recente
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )
    print(response)
    response = response.text
    print(response)

    return response