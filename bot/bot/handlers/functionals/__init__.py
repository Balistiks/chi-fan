from .instructors import instructor_router
from .salary import salary_router
from .gpt import gpt_routers
from .cash_report import cash_report_router

functionals_router = (*instructor_router, *salary_router, *gpt_routers, *cash_report_router)