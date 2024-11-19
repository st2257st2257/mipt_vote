from sqlalchemy import select
from database import new_session, StudentOrm, PoolOrm, AnswerOrm
from schemas import SStudentAdd, SStudent, SPoolId, SPoolAdd, SPool, SAnswer, SAnswerAdd, SAnswerId


class StudentRepository:
    @classmethod
    async def add_user(cls, student: SStudentAdd) -> int:
        async with new_session() as session:
            data = student.model_dump()
            new_student = StudentOrm(**data)

            session.add(new_student)
            await session.flush()
            await session.commit()
            return new_student.id

    @classmethod
    async def get_user(cls) -> list[SStudent]:
        async with new_session() as session:
            query = select(StudentOrm)
            result = await session.execute(query)
            student_models = result.scalars().all()
            students = [SStudent.model_validate(student_model) for student_model in student_models]
            return students


class PoolRepository:
    @classmethod
    async def add_pool(cls, pool: SPoolAdd) -> int:
        async with new_session() as session:
            data = pool.model_dump()
            new_pool = PoolOrm(**data)

            session.add(new_pool)
            await session.flush()
            await session.commit()
            return new_pool.id

    @classmethod
    async def get_pool(cls) -> list[SPool]:
        async with new_session() as session:
            query = select(PoolOrm)
            result = await session.execute(query)
            pool_models = result.scalars().all()
            pools = [SPool.model_validate(pool_model) for pool_model in pool_models]
            return pools


class AnswerRepository:
    @classmethod
    async def add_answer(cls, answer: SAnswerAdd) -> int:
        async with new_session() as session:
            data = answer.model_dump()
            new_answer = AnswerOrm(**data)

            session.add(new_answer)
            await session.flush()
            await session.commit()
            return new_answer.id

    @classmethod
    async def get_answer(cls) -> list[SAnswer]:
        async with new_session() as session:
            query = select(AnswerOrm)
            result = await session.execute(query)
            answer_models = result.scalars().all()
            answers = [SAnswer.model_validate(answer_model) for answer_model in answer_models]
            return answers
