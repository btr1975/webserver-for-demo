"""
Hello World Example # FIXME: This is an example you should delete it
"""
import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from webserver_for_demo.utils.logger import get_application_logger
LOGGER = get_application_logger().getChild(__name__)

router = APIRouter(
)

templates_path = os.path.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0], 'templates')
templates = Jinja2Templates(directory=templates_path)


@router.get('/hello', response_class=HTMLResponse, response_model=None,
            description='Hello World', name='Hello World', include_in_schema=False)
async def get_hello(request: Request) -> templates.TemplateResponse:
    """Function to display the Hello World

    :type request: fastapi.Request
    :param request: The request from the user

    :rtype: fastapi.templating.Jinja2Templates.TemplateResponse
    :returns: The webpage
    """
    host = request.client.host
    port = request.client.port
    LOGGER.info(f'get_hello received from {host}:{port}')
    error = None
    request_info = {}
    request_headers = {}

    try:
        for key, value in request.headers.items():
            request_headers[key] = value

        for key, value in request.items():
            if key == 'headers':
                continue
            request_info[key] = value

        LOGGER.info(f'get_hello data created')

    except Exception as err:  # pylint: disable=broad-except
        error = f'{err}'
        LOGGER.error(f'get_hello error: {error}')

    data = {
        'page': 'Hello World from webserver-for-demo',
        'request_info': request_info,
        'request_headers': request_headers,
        'error': error
    }

    return templates.TemplateResponse('index.jinja2', {'request': request, 'data': data})


@router.get('/hello-error', response_class=HTMLResponse, response_model=None,
            description='Hello World', name='Hello World', include_in_schema=False)
async def get_hello_error(request: Request) -> templates.TemplateResponse:
    """Function to display the Hello World

    :type request: fastapi.Request
    :param request: The request from the user

    :rtype: fastapi.templating.Jinja2Templates.TemplateResponse
    :returns: The webpage
    """
    host = request.client.host
    port = request.client.port
    LOGGER.info(f'get_hello_error received from {host}:{port}')

    try:
        raise Exception('OH NO THERE WAS SOME ERROR!!')

    except Exception as err:  # pylint: disable=broad-except
        error = f'{err}'
        LOGGER.error(f'get_hello error: {error}')

    data = {
        'page': 'Hello World Error from webserver-for-demo',
        'error': error
    }
    return templates.TemplateResponse('base.jinja2', {'request': request, 'data': data})
