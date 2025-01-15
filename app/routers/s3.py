from fastapi import APIRouter, HTTPException, status, UploadFile, File
import boto3
import os

s3 = boto3.client("s3")

router = APIRouter()

@router.get("/get_buckets/")
def get_buckets():
    s3_buckets = s3.list_buckets()
    return s3_buckets

@router.get("/get_bucket/{bucket_name}/")
def get_bucket(bucket_name: str):
    try:
        s3_bucket = s3.get_bucket_acl(Bucket=bucket_name)
        return s3_bucket
    except s3.exceptions.NoSuchBucket as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.get("/get_files/{bucket_name}/")
def get_files(bucket_name: str):
    try:
        s3_bucket = s3.list_objects(Bucket=bucket_name)
        return s3_bucket
    except s3.exceptions.NoSuchBucket as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.post("/upload_file/{bucket_name}/")
def upload_file(bucket_name: str, file: UploadFile = File(...)):
    try:
        print(file.filename)
        s3.upload_fileobj(file.file, bucket_name, file.filename)
        return {"message": f"File {os.path.basename(file.filename)} uploaded to bucket {bucket_name}"}
    except s3.exceptions.NoSuchBucket as e:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/create_bucket/")
def create_bucket(bucket_name: str):
    try:
        s3.create_bucket(Bucket=bucket_name)
        return {"message": f"Bucket {bucket_name} created"}
    except s3.exceptions.BucketAlreadyExists as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bucket name must be unique")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    

@router.delete("/delete_bucket/{bucket_name}/")
def delete_bucket(bucket_name: str):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        return {"message": f"Bucket {bucket_name} deleted"}
    except s3.exceptions.NoSuchBucket as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/delete_file/{bucket_name}/{file_name}/")
def delete_file(bucket_name: str, file_name: str):
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        return {"message": f"File {file_name} deleted from bucket {bucket_name}"}
    except s3.exceptions.NoSuchBucket as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except s3.exceptions.NoSuchKey as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))