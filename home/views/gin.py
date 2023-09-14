import asyncio

from django.http import StreamingHttpResponse
from django.template.loader import render_to_string, get_template
# from django.template.loader import

from home.recommendations import customized_recommendations


async def stream_homepage_content():
    for item in customized_recommendations:
        await asyncio.sleep(.7)  # Faking an expensive database query or slow API
        yield item


async def index(request):
    template = get_template('home.html')
    return StreamingHttpResponse(template.template.generate_async(dict(recommendations=stream_homepage_content())))
