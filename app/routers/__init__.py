from fastapi import APIRouter
from .users_router import router as users_router
from .get_groups.groups import router as get_groups_router
from .registration.registration_router import router as registration_router
from .schedule.schedule_router import router as schedule_router

router = APIRouter(prefix="/api")

router.include_router(users_router)
router.include_router(get_groups_router)
router.include_router(registration_router)
router.include_router(schedule_router)