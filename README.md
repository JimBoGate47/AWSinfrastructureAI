# AWSinfrastructureAI

# Overview
- Se crea una infraestructura basica con AWS CDK 
- Se cuenta con 2 buckets y funciones lambda 
- Se cargan las imagenes .tif en un bucket, y se dispara un trigger para su analisis
- Los resultados se guardan en un segundo bucket
- Para visualizar el estado/clasificacion se dispone de un enpdpoint publico (devuelve un HTML)

# Using
### Load image:
- aws s3 cp image.tif s3://s3bucketstack-bimbobucketv154ef298a-nv7meub40m9x

### View status:
En el Browser u otro método:

- curl https://mdtqyl6jjl.execute-api.us-east-1.amazonaws.com/

## Inconvenientes/Soluciones:
- Otorgar permisos/accesos de ejecución para los diferentes Stacks
- __Solucion__: se implementa AWS IAM
- textract timeout y error con la extension de imagenes tif
- __Solucion__: Textract ejecución asíncrona y se extiene el timeout 
- Errores con las dependencias externas para OpenAI
- __Solucion__: Se crea/añade layers sobre las funciones lambda que la requieran