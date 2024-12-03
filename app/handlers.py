"""
handlers.py

In this file we have custom exception handlers
"""

from fastapi import Request
from fastapi.responses import UJSONResponse


class UnicornException(Exception):
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg


async def unicorn_exception_handler(_request: Request, exc: UnicornException):
    return UJSONResponse(
        status_code=200,
        content={"errors": {"code": exc.code, "description": exc.msg}},
    )
