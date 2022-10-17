from pprint import pprint
from aiohttp import web
from aiohttp_jinja2 import setup, render_template
import jinja2
from text_analyzer.app import collecting
import scripts.indexing_api as Index_API
import json


DATA = dict()

async def handle_main(request):
    context = {'data' : None}
    response = render_template('index.html', request, context)
    return response


async def open_text_analyzer(request):
    context = {'data' : None}
    response = render_template('text_analyzer.html', request, context)
    return response


async def start_analysis(request):

    data = await request.post()

    main_text = data['main_text']
    comp_text = data['comp_text']
    result = collecting(main_text,comp_text)

    context = {
        'main' : result[0],
        'comp' : result[1],
        'info' : result[2],}

    response = render_template('text_analyzer_answer.html', request, context)
    return response


async def start_indexing(request):

    post_data = await request.post()
    data = {}

    if len(post_data) == 1:
        for k in set(post_data.keys()):
            data = json.loads(k, strict=False)
    else:
        for k in set(post_data.keys()):
            data[k] = post_data.getall(k)

    resp = Index_API.main(data['links'], data['token'][0])
    if resp == 0:
        response_obj = { 'status' : 'success' }
    else:
        response_obj = { 'status' : 'ERROR' }

    return web.Response(text=json.dumps(response_obj))


app = web.Application()

app.add_routes([web.get('/', handle_main),
                web.get('/text_analyzer', open_text_analyzer),
                web.post('/text_analyzer/statistics', start_analysis),
                web.post('/scripts/indexing_api', start_indexing),
                web.static('/static', 'tools/app/templates'),])


setup(app, loader=jinja2.FileSystemLoader('tools/app/templates'))


if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=5100)
    