import logging
from logging import Formatter

from flask import Flask, escape, render_template, request

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='[%(asctime)s %(name)s %(levelname)s] %(message)s',
                              datefmt="%b %d %H:%M:%S")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(ch)

@app.route('/', methods=['GET'])
def index():
    logger.debug("GET index")
    return render_template("index.html", name="John Doe")

@app.route('/hello', methods=['GET'])
def hello():
    logger.debug("GET hello")
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'