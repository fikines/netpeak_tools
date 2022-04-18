from aiohttp import web
from aiohttp_jinja2 import setup, render_template
import jinja2
from app import collecting
from flask import send_file

DATA = dict()

async def handle_main(request):
    context = {'data' : None}
    response = render_template('index.html', request, context)
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

    response = render_template('answer.html', request, context)
    return response


def get_tool():
    path = "test.txt"
    return send_file(path, as_attachment=True)


app = web.Application()

app.add_routes([web.get('/', handle_main),
                web.post('/statistics', start_analysis),
                web.static('/static', 'templates'),])


setup(app, loader=jinja2.FileSystemLoader('templates'))


if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=5100)
    