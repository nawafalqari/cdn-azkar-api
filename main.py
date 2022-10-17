from fastapi import FastAPI
from fastapi.responses import FileResponse
from uvicorn import run

app = FastAPI(title="AzkarAPI CDN", description="Azkar API CDN")

@app.get("/quran/{page}")
def quran_page(page:int):
   path = f"data/quran/{page}.jpg"
   try:
      with open(path):
         pass

      return FileResponse(f"data/quran/{page}.jpg")
   except:
      return {"err": True, "message": "invalid page number"}

if __name__ == "__main__":
   run("main:app", host="0.0.0.0", workers=3)