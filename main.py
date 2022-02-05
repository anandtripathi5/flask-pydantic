from flask import Flask

from dotenv import load_dotenv

from config import settings

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)


@app.get("/")
async def hello_world():
    template = f'''
    <p>Hello, {vars(settings)}!</p>
    '''
    return template

if __name__ == '__main__':
    app.run(port=settings.port)
