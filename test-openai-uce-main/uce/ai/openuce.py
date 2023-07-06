import openai
from pydantic import BaseModel


class Document(BaseModel):
    item: str = 'algoritmos'


def process_inference(user_prompt) -> str:
    openai.organization = 'org-ZWY7hnVw2WOKBgUCbZnaiRrz'
    openai.api_key = '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'
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación universitario que enumera los conceptos y técnicas que se deben aprender en la materia. 
             E.G. 
             Lenguajes de programacion:
             python
             java
             c++
             pascal},
             "role": "user", "content": user_prompt"""}
        ]
    )
    respuesta = completion.choices[0].message.content
    return respuesta
