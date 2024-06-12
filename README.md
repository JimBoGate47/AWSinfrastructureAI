# AItimall
## Basic requirements:
- aws cli
- pip
- npm
- IAM Configured

# Install dependencies:
- npm i

## In the jarvis folder run: 
- pip install -r requirements.txt
- cdk deploy --all

## Load image:
aws s3 cp imgpath s3://s3bucketstack-bimbobucketv154ef298a-nv7meub40m9x

# Inconvenientes/Soluciones:
- Otorgar permisos/accesos de ejecucion para los diferentes Stacks
- Solucion: se implementa AWS IAM
- textract timeout y error con la extension de imagenes tif
- Solucion: Textract ejecucion asincrona 