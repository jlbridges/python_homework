import logging




logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"Calling {func.__name__}")
        func()
        logger.log(logging.INFO,f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  returned: {result}")
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