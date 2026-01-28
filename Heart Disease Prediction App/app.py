import numpy as np
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from joblib import load
from pydantic import BaseModel

class PredictionInput(BaseModel):
    features: list[list[float]]

# App
app = FastAPI(debug=True)

BASE_DIR = Path(__file__).parent

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Load the trained model
model = load("model/Heart_disease_model.joblib")

@app.get("/")
async def preddiction_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/prediction")
async def preddiction(request: Request):
    return templates.TemplateResponse("formpage.html", {"request": request})

@app.post("/prediction")
async def predict(data: PredictionInput):

    try:
        
        X = np.array(data.features)

        # ---- Validation ----
        # Must be 2D
        if X.ndim != 2:
            raise HTTPException(
                status_code=400,
                detail="Input must be a 2D list"
            )

        # Must have exactly 13 features
        if X.shape[1] != 13:
            raise HTTPException(
                status_code=400,
                detail="Model expects exactly 13 features per sample"
            )

        # Optional scaling
        # X = scaler.transform(X)

        # Prediction
        prediction = model.predict(X)

        result = int(prediction[0])

        return {
            "prediction": result
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True)