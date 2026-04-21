import boto3
from starlette.responses import StreamingResponse
from urllib.parse import quote

from app.core.config import settings

s3 = boto3.client(
    "s3",
    endpoint_url=settings.S3_ENDPOINT,
    aws_access_key_id=settings.S3_ACCESS_KEY,
    aws_secret_access_key=settings.S3_SECRET_KEY,
)


def get_image_from_s3(key: str, group_name: str):
    response = s3.get_object(
        Bucket=settings.S3_BUCKET,
        Key=key
    )

    safe_filename = f"{group_name}.jpg"
    encoded_filename = quote(safe_filename)

    return StreamingResponse(
        response['Body'],
        media_type=response.get('ContentType', 'image/jpeg'),
        headers={
            "Content-Disposition": f"inline; filename={encoded_filename}; filename*=UTF-8''{encoded_filename}"
        }
    )
