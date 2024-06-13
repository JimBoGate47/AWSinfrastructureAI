# AWSinfrastructureAI

# Overview
- Se crea una infraestructura basica con AWS CDK 
- Se cuenta con 2 buckets y funciones lambda 
- Se cargan las imagenes .tif en un bucket, y se dispara un trigger para su análisis
- Los resultados se guardan en un segundo bucket
- Para visualizar el estado/clasificación se dispone de un enpdpoint público (devuelve un HTML)

# Usage
### Load image:
- aws s3 cp image.tif s3://main_s3bucket_name

### View status:
En el Browser u otro método (endpoint generada con AWS - Gateway):

- curl https://mdtqyl6jjl.execute-api.us-east-1.amazonaws.com/

## Inconvenientes/Soluciones:
- Otorgar permisos/accesos de ejecución para los diferentes Stacks
- __Solución__: se implementa AWS IAM
- textract timeout y error con la extension de imagenes tif
- __Solución__: Textract ejecución asíncrona y se extiene el timeout 
- Errores con las dependencias externas para OpenAI
- __Solución__: Se crea/añade layers sobre las funciones lambda que la requieran