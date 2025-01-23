from fastapi import APIRouter, HTTPException, status, UploadFile, File
import boto3
import os

s3 = boto3.client("s3")

router = APIRouter()

@router.get("/get_url_signed/")
def get_url_signed():
    try:
        bucker_name = "mi-bucket-s3-fastapi"
        file_name = "archivo_subir_s3.pdf"
        url = s3.generate_presigned_url(ClientMethod='get_object',
                                Params={'Bucket': bucker_name, 'Key': file_name},
                                ExpiresIn=3600, 
            )
        
        return {"url": url}
    except s3.exceptions.NoSuchBucket as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/post_url_signed/")
def post_url_signed(file: UploadFile = File(...)):
    try:
        bucker_name = "mi-bucket-s3-fastapi"
        
        
        url = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={'Bucket': bucker_name, 'Key': file.filename},
            ExpiresIn=3600, 
            HttpMethod='PUT',
        )
        
        return {"url": url}
    except s3.exceptions.NoSuchBucket as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))