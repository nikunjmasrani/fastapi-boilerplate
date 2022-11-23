from fastapi import APIRouter
from app.helper import response_helper
from app import constants, logger

router = APIRouter()

response_composer = response_helper.ResponseComposer()

# todo check db and redis connection in health api


@router.get('/health')
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """

    logger.info("DEBUG Health api getting called")
    return response_composer.make_response(
        message=constants.HEALTH_SUCCESS_RESPONSE
    )
