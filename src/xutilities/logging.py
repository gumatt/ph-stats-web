from dataclasses import dataclass
from json import dumps
from typing import List

from loguru import logger



DEFAULT_LOG_LEVEL: str = 'INFO'
DEFAULT_LOG_FORMAT: str = '<white> <b><level> {level: <8}</level></b> | <green>{time:DD HH:mm:ss:SSSS}</green> | <blue>{name}.{function}:{line}</blue> | <b>{message}</b></white>'
DEFAULT_LOG_SINK: str = 'std.err'


@dataclass
class LogSettings:
    level: str = DEFAULT_LOG_LEVEL
    msg_format: str = DEFAULT_LOG_FORMAT
    sink: str = DEFAULT_LOG_SINK


class Formatter:
    def __init__(self, config):
        self.padding = 0
        self.fmt = config.msg_format or DEFAULT_LOG_FORMAT
        
    def format(self, record):
        location_template = "{name}:{function}:{line}"
        length = len(location_template.format(**record))
        self.padding = max(self.padding, length)
        extra_format = ""
        if record["extra"]:
            record["extra"]["formatted"] = pretty(record["extra"])
            extra_format = "<yellow>{extra[formatted]}</yellow>" 
        record["extra"]["loc-padding"] = " " * (self.padding - length)
        return ''.join([self.fmt, "\n", extra_format, "\n"])


def pretty(obj):  # sourcery skip: instance-method-first-arg-name
    return dumps(obj, indent=2, sort_keys=True)


def init_logger(config: List[LogSettings]):
    logger.debug('Initializing logger with: {}', config)
    return logger
