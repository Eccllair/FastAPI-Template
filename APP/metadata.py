TITLE = "FastAPI-APP"
SUMMARY = "шаблон приложения FastAPI"
API_VERSION = "1"
DOCS_URL = "/docs"
OPENAPI_URL = "/openapi.json"
TAGS = [
    {"name": "products", "description": "действия продуктами."},
]
API_DESCRIPTION = """
Описание API
"""

ALLOW_ORIGINS=["http://localhost:5432"]
ALLOW_CREDITIONALS=True
ALLOW_METHODS=["*"]
ALLOW_HEADERS=["*"]