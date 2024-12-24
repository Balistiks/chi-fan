from .callbacks import callbacks_router
from .messages import messages_router

check_list_router = [callbacks_router, messages_router, ]