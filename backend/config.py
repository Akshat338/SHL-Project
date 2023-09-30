"""
  Project Management config file
"""
import os
from schemas.error_schema import (
    InternalServerErrorResponseModel,
    ValidationErrorResponseModel,
)

PORT = os.environ["PORT"] if os.environ.get("PORT") is not None else 80

ERROR_RESPONSES = {
    500: {
        "model": InternalServerErrorResponseModel
    },
    422: {
        "model": ValidationErrorResponseModel
    },
}
