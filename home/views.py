import asyncio

from django.http import StreamingHttpResponse
from django.template.loader import render_to_string

customized_recommendations = [
    dict(name='Comfy Chair', discount_price=745.00, normal_price=800.00, review_count=1550, img='product1.jpg'),
    dict(name='Bed King Size', discount_price=1055.00, normal_price=1599.99, review_count=720, img='product4.jpg'),
    dict(name='Lounge pairs', discount_price=350.00, normal_price=499.99, review_count=952, img='product2.jpg'),
    dict(name='Air mattress', discount_price=189.99, normal_price=250.00, review_count=153, img='product3.jpg'),
]


async def stream_homepage_content():
    pre_shell, post_shell = render_to_string('home/home.html').split('<!-- --- stream products --- -->')
    yield pre_shell
    for item in customized_recommendations:
        await asyncio.sleep(.7)  # Faking an expensive database query or slow API
        yield render_to_string('home/_item.html', dict(recommendation=item))
    yield post_shell


# Create your views here.
async def index(request):
    return StreamingHttpResponse(stream_homepage_content())
