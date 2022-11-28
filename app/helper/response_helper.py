from fastapi_utils.api_model import APIModel
from fastapi.responses import JSONResponse
from app import constants
from fastapi.encoders import jsonable_encoder
from fastapi import status


class BaseResponse(APIModel):
    message: str
    status: int
    payload: dict = {}

    @classmethod
    def request_exception_response(cls, exc):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {"message": "Validation Error", "payload": str(exc), "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY}
            ),
        )

    @classmethod
    def custom_exception_response(cls, message):
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={
            "message": message,
            "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "payload": {}
        })

    @classmethod
    def server_error_response(cls):
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={
            "message": constants.SOMETHING_WENT_WRONG,
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "payload": {}
        })



