from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

class NotFoundError(HTTPException):
    """Custom exception for resource not found."""
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)

class BadRequestError(HTTPException):
    """Custom exception for bad request."""
    def __init__(self, detail: str = "Bad request"):
        super().__init__(status_code=400, detail=detail)

class UnauthorizedError(HTTPException):
    """Custom exception for unauthorized access."""
    def __init__(self, detail: str = "Unauthorized access"):
        super().__init__(status_code=401, detail=detail)

class ForbiddenError(HTTPException):
    """Custom exception for forbidden access."""
    def __init__(self, detail: str = "Forbidden access"):
        super().__init__(status_code=403, detail=detail)

# Custom exception handlers
async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "path": str(request.url)}
    )

async def bad_request_handler(request: Request, exc: BadRequestError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "path": str(request.url)}
    )

async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "Validation error", "details": exc.errors(), "path": str(request.url)}
    )

# Registering exception handlers
def register_exception_handlers(app):
    """Function to register all custom exception handlers to the FastAPI app."""
    app.add_exception_handler(NotFoundError, not_found_handler)
    app.add_exception_handler(BadRequestError, bad_request_handler)
    app.add_exception_handler(ValidationError, validation_error_handler)


