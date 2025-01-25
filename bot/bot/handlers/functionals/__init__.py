from .instructors import instructor_router
from .salary import salary_router
from .gpt import gpt_routers
from .cash_report import cash_report_router
from .new_employee import new_employee_router
from .swap import swap_router

functionals_router = (*instructor_router, *salary_router, *gpt_routers, *cash_report_router,
                      *new_employee_router, *swap_router,)