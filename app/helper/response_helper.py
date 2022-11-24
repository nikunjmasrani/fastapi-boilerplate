from fastapi_utils.api_model import APIModel


class BaseResponse(APIModel):
    message: str
    status: int
    payload: dict = {}










