from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import groq 
app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/infer")
async def infer(input: TextInput):
    try:
       
        result = groq.inference(input.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
