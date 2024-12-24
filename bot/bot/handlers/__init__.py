from .messages import messages_router
from .callbacks import callbacks_router
from .functionals import functionals_router
from .check_list import check_list_router

routers = [messages_router, *functionals_router, callbacks_router, *check_list_router, ]