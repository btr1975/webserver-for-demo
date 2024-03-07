"""
This is an example FIXME: Example delete this
"""
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from webserver_for_demo.utils.schemas import ErrorSchema
from webserver_for_demo.utils.logger import get_application_logger
LOGGER = get_application_logger().getChild(__name__)


router = APIRouter(
    prefix='/api/v1',
    responses={400: {'model': ErrorSchema}, 401: {'model': ErrorSchema}},
    tags=['example']
)


class ResponseSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Schema for example"""
    response: str


@router.get('/example/{name}',
             responses={200: {'model': ResponseSchema}},
             description='This is an example',
             name='Example endpoint')
async def get_example(name: str, request: Request) -> ResponseSchema:
    """Function for the example endpoint

    :type name: String
    :param name: A name
    :type request: fastapi.Request
    :param request: The request from the user

    :rtype: ResponseSchema
    :returns: The JSON Data

    :raises HTTPException: If anything goes wrong
    """
    host = request.client.host
    port = request.client.port
    LOGGER.info(f'get_example received from {host}:{port}')
    try:
        result = ResponseSchema(response=name)

    except Exception as error:  # pragma: no cover
        LOGGER.error(f'get_example error: {error}')
        raise HTTPException(status_code=400, detail=f'{error}') from error

    return result
