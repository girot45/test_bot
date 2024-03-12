from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.src.database import UserQuery


async def insert_user_query(session, user_id, product_code):
    try:
        new_query = UserQuery(
            user_id=user_id,
            product_code=product_code,
        )
        session.add(new_query)
        await session.commit()
        await session.close()
        return {"mes": "success", "status": True}
    except SQLAlchemyError as e:
        await session.rollback()
        return {"mes": f"error {str(e)}", "status": False}

async def get_last_5_queries(session: AsyncSession):
    try:
        stmt = (
            select(UserQuery)
            .order_by(UserQuery.timestamp.desc())
            .limit(5)
        )
        res = await session.execute(stmt)
        query = res.all()
        await session.close()
        return {"mes": "success", "data": query}
    except SQLAlchemyError as e:
        return {"mes": f"error {str(e)}", "data": None}
