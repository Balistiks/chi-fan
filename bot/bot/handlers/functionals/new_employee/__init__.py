from .callbacks import callbacks_router
from .messages import messages_router

new_employee_router = [callbacks_router, messages_router,]