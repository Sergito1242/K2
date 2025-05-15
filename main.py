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

    url_make = "https://hook.us2.make.com/ssvzclvzp9qgk9bkfhrjnqs5o9o4emk2"  # tu webhook real

    try:
        r = requests.post(url_make, json=datos)
        print("🔁 Texto crudo de Make:", r.text)
        print("📦 Headers:", r.headers)

        return {
            "status": r.status_code,
            "respuesta": r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text
        }
    except Exception as e:
        return {"error": str(e)}

