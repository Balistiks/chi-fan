from .callbacks import callbacks_router
from .messages import messages_router

gpt_routers = [callbacks_router, messages_router]