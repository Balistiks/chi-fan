from .callbacks import callbacks_router
from .messages import messages_router

cash_report_router = [callbacks_router, messages_router]