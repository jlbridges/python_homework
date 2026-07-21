import logging

# Task 1: Writing and Testing a Decorator

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional = list(args) if args else "none"
        keyword = dict(kwargs) if kwargs else "none"

        # One grouped record per invocation, so each call's four pieces of
        # information stay together as a single log entry.
        logger.log(
            logging.INFO,
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {result}\n"
        )
        return result
    return wrapper


# takes no parameters, returns nothing
@logger_decorator
def hello():
    print("Hello, World!")


# takes a variable number of positional arguments, returns True
@logger_decorator
def new_func(*args):
    return True


# takes no positional arguments, a variable number of keyword arguments, returns logger_decorator
@logger_decorator
def new_new_func(**kwargs):
    return logger_decorator


# mainline: call each function, passing parameters where applicable
hello()
new_func('test')
new_new_func(test='test2', another='value2')