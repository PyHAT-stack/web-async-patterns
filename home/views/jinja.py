import asyncio

from django.http import StreamingHttpResponse
from django.template.loader import get_template

from home.recommendations import customized_recommendations


async def stream_homepage_content():
    for item in customized_recommendations:
        # Faking an expensive database query or slow API
        await asyncio.sleep(.7)
        yield item


async def index(request):
    template = get_template('home.html')
    return StreamingHttpResponse(
        template.template.generate_async({
            'recommendations': stream_homepage_content()
        })
    )
