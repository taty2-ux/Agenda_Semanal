import pandas as pd
from io import StringIO

def baixar_csv(response):
    try:
        response = response.replace("```csv", "").replace("```", "").strip() 
        tabela = pd.read_csv(StringIO(response))
        tabela.to_csv("app/apk/horarios.csv", index=False, sep=";", encoding="utf-8-sig")

    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")