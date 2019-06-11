
from sanic import Sanic
from sanic.response import json

app = Sanic('LeyStudyApp')
app.config.DB_NAME = 'ley_study'
app.config.DB_USER = 'zhanglei'

@app.route('/')
async def test(request):
    print(request.header)
    print(request.body)
    msg = {'message': 'Welcom to 老张学Python'}
    return json(msg, ensure_ascii=False)

@app.route('/api/login')
async def test1(request):
    print(request)
    msg = {'message': '访问了老张的Login了！'}
    return json(msg, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='35.184.71.227', port=8899)
    # app.run(host='192.168.11.195', port=8899)