from dataclasses import dataclass, field
from typing import List

from src.xutilities.logging import LogSettings


def default_log_settings_factory():
    settings = LogSettings(
        level='DEBUG',
        sink='sys.stderr'
    )
    return [settings]

@dataclass
class AppSettings():
    name: str = 'Default App Name'
    logging: List[LogSettings] = field(default_factory=default_log_settings_factory)
