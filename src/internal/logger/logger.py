import logging
from pythonjsonlogger import json

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logHandler = logging.StreamHandler()
    fmt = json.JsonFormatter(
        "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s",
        rename_fields={
            "levelname": "level",
            "asctime": "ts",
            "filename": "caller",
            "lineno": "line",
            "message": "msg",
        },
    )
    logHandler.setFormatter(fmt)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

    return logger
