from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def test(request):
    return json({'message': 'Hello World'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
