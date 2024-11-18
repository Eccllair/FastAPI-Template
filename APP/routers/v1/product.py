from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database import get_async_session
from schemas.product import ProductSchema
from sqlalchemy.ext.asyncio import AsyncSession
from controllers.product import get_product_query


product_router = APIRouter()


@product_router.get("/", response_model=List[ProductSchema])
async def get_product(
    id: int,
    name: Optional[str],
    session: AsyncSession = Depends(get_async_session),
):
    """
    возвращает продукт по id
    """
    try:
        response = JSONResponse(
            body=await get_product_query(session, id)
        )
    except ValueError as e:
        HTTPException(422, str(e))
    return response