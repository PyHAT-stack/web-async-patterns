# Proof of concept: Streaming HTML in Django

Inspired by Taylor Hunt's incredible explanation of how he turned [a slow Fortune 20 webapp into a snappy experience, even on a cheap Android phone](https://dev.to/tigt/making-the-worlds-fastest-website-and-other-mistakes-56na), I made this repo to show the current capability of Django to render streaming HTML.

This technique is best used to improve the perceptual performance for expensive database queries or slow API calls. The idea is that the user could start seeing the page come together while the query or calls are happening. Rendering of the page will pause once it hits the block that is waiting on the data, but being able to see the page render should make the user feel as though the website is performing faster.

Referencing Taylor's blog post:

> Both of [these pages](https://assets.codepen.io/183091/HTML+streaming+vs.+non.mp4) show search results in 2.5 seconds. But they sure don't _feel_ the same.

This concept shows how a recommendation engine takes some time to recommend four products, based for the current user.

## Viewing the concept

Open a terminal at the root of this project and type the following:

```shell
python -m venv .venv --prompt strm_django
# If in Windows:
.venv/Scripts/activate
# otherwise
source .venv/bin/
# Then
pip install -r requirements.txt
uvicorn stream.asgi:application --reload 
```

You can then click the link in the terminal or go to http://127.0.0.1:8000 to view the page.
