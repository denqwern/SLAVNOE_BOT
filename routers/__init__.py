__all__ = ("router",)

from aiogram import Router

from .send_message import router as send_message

from .survay import router as survay

router = Router()
router.include_router(send_message)

router.include_router(survay)
