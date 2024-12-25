from .instructors import instructor_router
from .salary import salary_router
from .gpt import gpt_routers
from .check_list import check_list_router

functionals_router = (*instructor_router, *salary_router, *gpt_routers, *check_list_router, )