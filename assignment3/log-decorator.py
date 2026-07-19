import logging


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper
@logger_decorator
def hello():
    print("Hello, World!")
@logger_decorator
def new_func(*args):
    return True
@logger_decorator
def new_new_func(**kwargs):
    return logger_decorator(hello)

hello()
new_func('test')
new_new_func(test = 'test2')