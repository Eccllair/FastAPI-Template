from models.main import Base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import (
    Integer,
    Sequence,
    String
)

class Product(Base):
    """общие задачи для получения монет"""

    __tablename__ = "fastapi_product"

    id: Mapped[int] = mapped_column(
        "id", Integer(), Sequence("fastapi_tasks_id_seq"), primary_key=True
    )
    name: Mapped[str] = mapped_column(type_=String(127), default="")