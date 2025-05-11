from aiogram import Router

from .commands import router as commands_router
from .info import router as info_router
from .settings import router as settings_router


router = Router()
router.include_router(commands_router)
router.include_router(info_router)
router.include_router(settings_router)
