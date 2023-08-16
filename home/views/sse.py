import asyncio
import random
import re

from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from home.recommendations import customized_recommendations


def index(request):
    return render(request, 'home/home_sse.html')


async def sse_recommendation():
    recommendations = []
    for item in customized_recommendations:
        await asyncio.sleep(.7)
        content = render_to_string('home/_item.html', dict(recommendation=item))
        recommendations.append(
            re.sub('\n', '', content)
        )
    all_recommendations = ''.join(recommendations)
    yield f'data: {all_recommendations}\n\n'


def handle_sse(request):
    return StreamingHttpResponse(streaming_content=sse_recommendation(), content_type='text/event-stream')
