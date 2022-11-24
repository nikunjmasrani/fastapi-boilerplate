from fastapi import Depends, status
from app import constants
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.web.profile.response import ProfileResponse
from app.web.profile.validator import Profile
from app.services.db.dependencies import get_db_session
router = InferringRouter()


@cbv(router)
class Profile:
    @router.post('/')
    async def get_profile(self, profile: Profile, db=Depends(get_db_session)) -> ProfileResponse:
        print("DEBUG")
        response = await db.execute('SELECT * FROM user')
        print(response)
        return ProfileResponse(message=constants.PROFILE_GET_SUCCESS_RESPONSE, status=status.HTTP_200_OK)
