"""
FastAPI WebApp
"""

import os
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from webserver_for_demo.version import __version__
from webserver_for_demo.routers import example

from webserver_for_demo.routers import hello_world

static_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')


# Used to config swagger UI
# Reference : https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
swagger_ui_parameters = {
    'docExpansion': 'none',
    'filter': 'true'
}

web_app = FastAPI(
    title='webserver-for-demo',
    version=__version__,
    description='Just a Webserver for Demo',
    swagger_ui_parameters=swagger_ui_parameters,
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

@web_app.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def get_docs() -> HTMLResponse:
    """Get Swagger UI HTML at the /docs endpoint redirected from the /docs endpoint

    :rtype: HTMLResponse
    :return: Swagger UI HTML
    """
    return get_swagger_ui_html(openapi_url="/docs/openapi.json", title="docs")


@web_app.get("/redoc", response_class=HTMLResponse, include_in_schema=False)
async def get_redoc() -> HTMLResponse:
    """Get ReDoc HTML at the /redoc endpoint redirected from the /redoc endpoint

    :rtype: HTMLResponse
    :return: ReDoc HTML
    """
    return get_redoc_html(openapi_url="/docs/openapi.json", title="redoc")


@web_app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json() -> dict:
    """Get OpenAPI JSON at the /openapi.json endpoint redirected from the /openapi.json endpoint

    :rtype: dict
    :return: OpenAPI JSON
    """
    return get_openapi(title=web_app.title, version=web_app.version, routes=web_app.routes)

web_app.include_router(example.router)

web_app.include_router(hello_world.router)

web_app.mount("/static", StaticFiles(directory=static_path), name="static")
