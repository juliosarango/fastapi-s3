from fastapi import FastAPI, Request

from .routers import s3

app = FastAPI()
app.include_router(s3.router, prefix="/s3", tags=["AWS bucket S3"])
