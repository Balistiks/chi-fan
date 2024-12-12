from .instructors import instructor_router
from .salary import salary_router
from .gpt import gpt_routers

functionals_router = (*instructor_router, *salary_router, *gpt_routers, )