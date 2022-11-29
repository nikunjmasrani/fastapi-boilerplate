from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from app import constants
from pydantic import BaseModel


class BaseResponse(BaseModel):
    message: str
    status: int
    payload: dict = {}

    @classmethod
    async def request_exception_response(cls, translator, exc):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {
                    "message": translator(constants.VALIDATION_ERROR),
                    "payload": str(exc),
                    "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
                }
            ),
        )

    @classmethod
    async def custom_exception_response(cls, translator, message):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "message": translator(message),
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "payload": {},
            },
        )

    @classmethod
    async def server_error_response(cls, translator):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": translator(constants.SOMETHING_WENT_WRONG),
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "payload": {},
            },
        )
