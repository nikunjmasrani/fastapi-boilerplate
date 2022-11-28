import asyncio

from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.web.monitor.response import HealthResponse
from app import constants, logger
from fastapi.requests import Request

router = InferringRouter()




@cbv(router)
class Monitor:
    @router.get('/health')
    async def health_check(self, request: Request) -> HealthResponse:
        logger.debug(f"Health api started: {request.state.request_id}")
        await asyncio.sleep(3)
        """
        Checks the health of a project.

        It returns 200 if the project is healthy.
        """
        """
         todo add db, redis, es network call to check health in system.
        """
        logger.debug(f"Health api competed: {request.state.request_id}")
        return HealthResponse(
            status=constants.HTTP_200_,
            message=constants.HEALTH_SUCCESS,
            payload={}
        )
