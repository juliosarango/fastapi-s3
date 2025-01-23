from fastapi import FastAPI, Request

from .routers import s3, url_signed


app = FastAPI()
app.include_router(s3.router, prefix="/s3", tags=["AWS bucket S3"])
app.include_router(url_signed.router, prefix="/signed", tags=["AWS bucket S3 signed urls"])
