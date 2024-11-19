from fastapi import APIRouter, Depends

from repository import StudentRepository, PoolRepository, AnswerRepository
from schemas import \
    SStudentAdd, SStudentId, SStudent, \
    SAnswerAdd, SAnswer, SAnswerId, \
    SPool, SPoolAdd, SPoolId


router = APIRouter(
    prefix="/api",
    tags=["Опросы"],
)


@router.post(
        "/students",
        description="Добавляет пользователя",
        summary="Добавляет пользователя",
        response_description="Вот такой ответ придет",
)
async def add_user(task: SStudentAdd = Depends()) -> SStudentId:
    new_task_id = await StudentRepository.add_user(task)
    return {"id": new_task_id}


@router.get("/students")
async def get_user() -> list[SStudent]:
    tasks = await StudentRepository.get_user()
    return tasks


@router.post(
        "/pools",
        description="Добавляет пользователя",
        summary="Добавляет пользователя",
        response_description="Вот такой ответ придет",
)
async def add_pool(pool: SPoolAdd = Depends()) -> SPoolId:
    new_pool_id = await PoolRepository.add_pool(pool)
    return {"id": new_pool_id}


@router.get("/pools")
async def get_pool() -> list[SPool]:
    pools = await PoolRepository.get_pool()
    return pools


@router.post(
        "/answers",
        description="Добавляет пользователя",
        summary="Добавляет пользователя",
        response_description="Вот такой ответ придет",
)
async def add_answer(answer: SAnswerAdd = Depends()) -> SAnswerId:
    new_answer_id = await AnswerRepository.add_answer(answer)
    return {"id": new_answer_id}


@router.get("/answers")
async def get_answer() -> list[SAnswer]:
    answers = await AnswerRepository.get_answer()
    return answers
