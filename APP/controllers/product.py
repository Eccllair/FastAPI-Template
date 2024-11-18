from sqlalchemy import select
from models.product import Product
from schemas.product import ProductSchema
from sqlalchemy.ext.asyncio import AsyncSession


async def get_product_query(
    session: AsyncSession, id: int
) -> ProductSchema:
    tasks_and_products = (
        (
            await session.execute(
                select(Product).where(
                    Product.id == id
                )
            )
        )
        .scalars()
        .one()
    )
    return ProductSchema(**tasks_and_products)
