from .instructors import instructor_router
from .salary import salary_router

functionals_router = (*instructor_router, *salary_router, )