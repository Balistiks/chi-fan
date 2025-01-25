from .instructors import instructor_router
from .salary import salary_router
from .gpt import gpt_routers
from .cash_report import cash_report_router
from .new_employee import new_employee_router
from .swap import swap_router
from .analitic import analitic_router
from .change_employee import change_employee

functionals_router = (
    *instructor_router,
    *salary_router,
    *gpt_routers,
    *cash_report_router,
    *new_employee_router,
    *analitic_router,
    *change_employee,
    *swap_router
)
