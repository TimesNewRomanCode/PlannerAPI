import boto3
from botocore.exceptions import ClientError
from fastapi import HTTPException, status
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
    try:
        response = s3.get_object(
            Bucket=settings.S3_BUCKET,
            Key=key
        )
    except ClientError as exc:
        error_code = exc.response.get("Error", {}).get("Code")
        if error_code in {"NoSuchKey", "404", "NotFound"}:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Schedule image not found: {key}",
            ) from exc
        raise

    safe_filename = f"{group_name}.jpg"
    encoded_filename = quote(safe_filename)

    return StreamingResponse(
        response['Body'],
        media_type=response.get('ContentType', 'image/jpeg'),
        headers={
            "Content-Disposition": f"inline; filename={encoded_filename}; filename*=UTF-8''{encoded_filename}"
        }
    )
