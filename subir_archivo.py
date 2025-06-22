import boto3
import base64

def lambda_handler(event, context):
    # Entrada
    bucket = event['body']['bucket']
    directorio = event['body'].get('directorio', '/')
    archivo = event['body']['archivo']
    base64_str = event['body']['base64']

    # Verificar que el directorio termine con '/'
    if not directorio.endswith('/'):
        directorio += '/'
    
    # Proceso
    s3 = boto3.client('s3')
    try:
        # Decodificamos el archivo de base64
        archivo_decodificado = base64.b64decode(base64_str)
        
        # Subir el archivo al bucket S3
        s3.put_object(Bucket=bucket, Key=directorio + archivo, Body=archivo_decodificado)
        
        message = f"Archivo '{archivo}' subido exitosamente al bucket '{bucket}' en el directorio '{directorio}'."
        estado = 200
    except Exception as e:
        message = f"Error al subir el archivo: {str(e)}"
        estado = 500
    
    # Salida
    return {
        'statusCode': estado,
        'message': message
    }