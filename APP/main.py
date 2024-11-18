from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from metadata import (
    TAGS,
    API_DESCRIPTION,
    TITLE,
    SUMMARY,
    DOCS_URL,
    OPENAPI_URL,
    API_VERSION,
    ALLOW_CREDITIONALS,
    ALLOW_HEADERS,
    ALLOW_METHODS,
    ALLOW_ORIGINS,
)
from configs.config import LOG_PATH
from routers.product import product_router

app = FastAPI(
    title=TITLE,
    description=API_DESCRIPTION,
    summary=SUMMARY,
    version=API_VERSION,
    openapi_tags=TAGS,
    docs_url=DOCS_URL,
    openapi_url=OPENAPI_URL,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDITIONALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)


logging.basicConfig(filename=LOG_PATH, level=logging.INFO)

app.include_router(
    router=product_router, prefix=f"/myapp/{API_VERSION}/products", tags=["products"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
