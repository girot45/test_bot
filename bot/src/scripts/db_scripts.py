import asyncio

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.src.database import UserQuery


async def insert_user_query(
        session: AsyncSession,
        user_id,
        product_code
):
    new_query = UserQuery(
        user_id=user_id,
        product_code=product_code,
    )
    session.add(new_query)
    await session.commit()
    await session.close()


async def get_last_5_queries(session: AsyncSession):
    stmt = (
        select(UserQuery)
        .order_by(UserQuery.timestamp.desc())
        .limit(5)
    )
    res = await session.execute(stmt)
    query = res.all()
    await session.close()
    return query
