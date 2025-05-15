from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "🟢 API activa"}

@app.post("/enviar")
async def enviar(request: Request):
    datos = await request.json()
    print("➡️ Recibido:", datos)

    url_make = "https://hook.us2.make.com/xxxxx"  # tu webhook real

    try:
        r = requests.post(url_make, json=datos)
        return {
            "status": r.status_code,
            "respuesta": r.json() if r.headers.get("content-type") == "application/json" else r.text
        }
    except Exception as e:
        return {"error": str(e)}
