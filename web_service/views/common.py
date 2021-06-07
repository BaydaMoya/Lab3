from aiohttp import web
from aiohttp_apispec import request_schema, response_schema

from ..schemas.common import FreeTextHandler, PingResponse


async def index_handler(_):
    raise web.HTTPFound('/swagger')


@response_schema(PingResponse)
async def ping_handler(_):
    return web.json_response({'ping': 'pong'})


@request_schema(FreeTextHandler)
async def free_text_handler(request):
    request_body = await request.json()
    request_text = request_body['text']


#My bayda yeee:
    # TODO: implement your handler logic here, for example:
    if '400' in request_text:
        raise web.HTTPBadRequest(
            reason='400 Bad Request Error. Need to upload client cert onto browser, bro')

    return web.json_response({'status': 'ok'})
