from app import logger
from fastapi import Request, status
from app import constants
from app.exception import CustomException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import time
import uuid


class ProfilerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):

        """
        Middleware class performs
         1. add request_id to track execution
         2. logs processing time
         3. handle server side exception globally.
        """

        request_id = str(uuid.uuid4())
        start_time = time.time()
        try:
            request.state.request_id = request_id
            response = await call_next(request)
            process_time = time.time() - start_time
            response.headers["X-Process-Time"] = str(process_time)
            response.headers['Request-ID'] = request_id
            logger.info(f"RequestID: {request_id} -> Path {request.url.path} -> Time Taken: {process_time}")
            if process_time >= 2:
                logger.warn(f"RequestID: {request_id} Taking more than 2 seconds please review the code.")
            return response

        except CustomException as ce:
            return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={
                "message": ce.name,
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "payload": {}
            })
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            logger.error(f"RequestID: {request_id} -> Path {request.url.path} Error: {str(e)}")
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={
                "message": constants.SOMETHING_WENT_WRONG,
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "payload": {}
            })




