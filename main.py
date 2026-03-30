from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "api masuk mas bro"}

@app.post("/predict")
def predict(data: dict):
    text = data.get("text")
    
    # dummy klasifikasi dulu
    if "jalan" in text.lower():
        kategori = "infrastruktur"
    else:
        kategori = "lainnya"

    return {
        "text": text,
        "kategori": kategori
    }