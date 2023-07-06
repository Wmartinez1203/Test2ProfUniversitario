from fastapi import FastAPI

from uce.ai.openuce import Document, process_inference

app: FastAPI = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/inference", status_code=200)
def inference(doc: Document):
    conceptos = process_inference(doc.item)
    return {
        'Respuesta:': conceptos
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=9062)