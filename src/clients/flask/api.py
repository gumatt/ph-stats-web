import sys

from flask import Flask

from src.clients.types import AppSettings
from src.xutilities.logging import DEFAULT_LOG_FORMAT, pretty, logger, Formatter



def create_app(config: AppSettings):
    api = Flask(config.name)
    api.logger = config_logging(config)
    return api


def config_logging(config: AppSettings):
    logger.debug('Initializing logger with: {}', config)
    handlers = []
    for cfg in config.logging:
        formatter = Formatter(cfg)
        sink = cfg.sink if 'sys.' not in cfg.sink else eval(cfg.sink)
        handlers.append({'sink': sink, 'format': formatter.format, 'level': cfg.level})
    if handlers:
        logger.remove()
        logger.configure(handlers=handlers)
    logger.info('logger.info message (after config applied)')
    return logger