# Boto3 S3 API FastAPI
![Boto3 S3 API FastAPI](images/s3-python-boto3.webp)

## Requisitos

- Python 3.11 o superior
- FastAPI
- Boto3

## Instalación

```bash
git clone https://github.com/juliosarango/fastapi-s3.git
cd fastapi-s3
python -m venv venv_fastapi_s3
source venv_fastapi_s3/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
cd app
fastapi dev
```
![Run FastAPI](images/run_api.png)

## API
Navegar a la ruta `http://localhost:8000/docs` para ver la API
![API](images/api.png)

## Configuración en AWS 
Para seguir la configuración de políticas en IAM de AWS, siga los pasos indicados en el [siguiente post](https://)
