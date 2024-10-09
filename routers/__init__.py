__all__=("router", )
from aiogram import Router
#from .commands import router as commands_router
from .send_message import router as send_message

from .survay import router as survay

router = Router()
#router.include_router(commands_router)
router.include_router(send_message)

router.include_router(survay)

