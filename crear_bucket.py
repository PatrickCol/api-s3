import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_region = event['body'].get('region', 'us-east-1')  # Región por defecto

    # Proceso
    s3 = boto3.client('s3', region_name=nombre_region)
    try:
        if nombre_region == 'us-east-1':
            s3.create_bucket(Bucket=nombre_bucket)
        else:
            location = {'LocationConstraint': nombre_region}
            s3.create_bucket(Bucket=nombre_bucket, 
                             CreateBucketConfiguration=location
                            )
        message = f"Bucket '{nombre_bucket}' creado exitosamente."
        estado = 200
    except ClientError as e:
        message = f"Error al crear el bucket '{nombre_bucket}': {str(e)}"
        estado = 500

    # Salida
    return {
        'statusCode': estado,
        'message': message
    }