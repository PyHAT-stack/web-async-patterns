import asyncio

from django.http import StreamingHttpResponse
from django.template.loader import render_to_string

from home.recommendations import customized_recommendations


async def stream_homepage_content():
    pre_shell, post_shell = render_to_string('home/home.html').split('<!-- --- stream products --- -->')
    yield pre_shell
    for item in customized_recommendations:
        await asyncio.sleep(.7)  # Faking an expensive database query or slow API
        yield render_to_string('home/_item.html', dict(recommendation=item))
    yield post_shell


async def index(request):
    return StreamingHttpResponse(stream_homepage_content())
