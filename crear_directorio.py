import boto3

import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Entrada (json)
    bucket = event['body']['bucket']
    carpeta = event['body']['carpeta']

    # Validar que termine con '/'
    if not carpeta.endswith('/'):
        carpeta += '/'

    # Proceso
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=bucket, Key=carpeta)
        message = f"Directorio '{carpeta}' creado en el bucket '{bucket}'."
        estado = 200
    except ClientError as e:
        message = f"Error al crear el directorio: {str(e)}"
        estado = 500

    # Salida
    return {
        'statusCode': estado,
        'message': message
    }
