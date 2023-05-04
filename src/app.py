import os

from flask import jsonify

from .modules.use_cases import logging_test_uc1
from .clients.types import AppSettings
from .clients.flask.api import create_app



config = AppSettings()

app = create_app(config)


@app.route('/')
def hello_world():
    my_env = os.getenv('FLASK_ENV')
    return jsonify({'env': my_env})


@app.route('/log_test')
def log_test():
    with app.logger.contextualize(trace_id='trace_id_0001'):
        app.logger.info('starting log_text use case')
        logging_test_uc1(info='this is payload info', logger=app.logger)
        app.logger.info('ending log_text use case')
    return jsonify({'status': 'done'})
