from fastapi import Depends, status
from app import constants
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.web.profile.response import ProfileResponse
from app.web.profile.validator import Profile as ProfileValidator
from app.web.profile.service import Profile as ProfileService
from app.services.db.dependency import get_db_session
from app.services.es.dependency import get_es_client
from app.services.redis.dependency import get_redis_pool
router = InferringRouter()


@cbv(router)
class Profile:

    @router.post('/')
    async def create_profile(self,
                             profile: ProfileValidator,
                             db=Depends(get_db_session),
                             es_client=Depends(get_es_client),
                             redis_client=Depends(get_redis_pool)) -> ProfileResponse:
        profile_service = ProfileService(db, es_client, redis_client)
        response = await profile_service.create(profile)
        return ProfileResponse(payload=response,
                               message=constants.PROFILE_CREATED_SUCCESS,
                               status=status.HTTP_200_OK)

    @router.get('/')
    async def get_profile(self, user_id: int, db=Depends(get_db_session)):
        profile_service = ProfileService(db)
        response = await profile_service.get(user_id)
        return ProfileResponse(payload=response,
                               message=constants.PROFILE_GET_SUCCESS,
                               status=status.HTTP_200_OK)
