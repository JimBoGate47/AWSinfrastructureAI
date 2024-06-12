# AItimall
## Basic requirements:
- aws cli
- pip
- npm
- IAM Configured

# Install dependencies:
- npm i

## Into jarvis folder:
- pip install -r requirements.txt
- cdk deploy --all

# Overview
- Se crea una infraestructura basica con 2 buckets y funciones lambda 
- Se cargan las imagenes .tif en un bucket, y se dispara un trigger para su analisis
- Los resultados se guardan en un segundo bucket
- Para visualizar el estado se dispone de un enpdpoint publico

## Inconvenientes/Soluciones:
- Otorgar permisos/accesos de ejecucion para los diferentes Stacks
- \textbf{Solucion}: se implementa AWS IAM
- textract timeout y error con la extension de imagenes tif
- Solucion: Textract ejecucion asincrona y se extiene el timeout 
- Errores con las dependencias externas
- Solucion: Se añade layers sobre las funciones lambda

criterio: "si encuentras una linea o frase que empiece con 'R' seguido por numeros y una fecha o que previamente mencione que se adjunta sera clasificado como 'no normativa' por el contrario sera 'normativa'"

agrego texto y quiero que respondas si es 'normativa' o 'no normativa' y solo eso

## Uso
### Load image:
aws s3 cp imgpath s3://s3bucketstack-bimbobucketv154ef298a-nv7meub40m9x

### View status:
curl https://mdtqyl6jjl.execute-api.us-east-1.amazonaws.com/