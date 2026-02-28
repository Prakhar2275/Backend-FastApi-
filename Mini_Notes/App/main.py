from fastapi import FastAPI

app=FastAPI(
    title="Notes API",
    description="FastApi Backend for mini notes management system",
    version="1.0.0"
)

@app.get("/")

def root():
    return {"message":"Api is running"}