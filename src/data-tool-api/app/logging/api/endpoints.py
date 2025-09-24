from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from app.common.logger.interfaces import ILogger
from app.container import Container

router = APIRouter(prefix="/logging")

@router.get("/log", summary="Log messages using all ILogger methods")
@inject
def log_message(
    logger: ILogger = Depends(lambda: Container.logger())
):
    """
    Log messages using all ILogger methods.

    Returns:
        dict: Confirmation message.
    """
    logger.info("Info log")
    logger.warning("Warning log")
    logger.error("Error log")
    logger.critical("Critical log")
    logger.info("Interpolated : Hello, {name}! Your score is {score}.", {"name": "John", "score": "100"})
    logger.error("MyLogMessage \n\r type : {exception_type}\n\r message: {exception_message}\n\r stacktrace: {exception_stacktrace}", {"exceptionmessage": "m...", "exceptiontype": "t...", "exceptionstacktrace": "s...."})

    try:
        raise Exception("MY EXCEPTION MESSAGE")
    except Exception as exception_occurred:
        logger.error("An error occured", exception_occurred)
        # raise 
        pass

    return {"message": "All log levels executed."}