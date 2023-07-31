from functools import wraps
from time import sleep
from Decorator.exceptions import RetryAPIException


def retry_decorator(retry_limit=3, sleep_time=60, quiet=True):  # Sleep time in seconds
    def decorator(func):

        @wraps(func)
        def retry(*args, **kwargs):
            retry_count = 0
            while retry_count < retry_limit:
                try:
                    return func(*args, **kwargs)
                except RetryAPIException as e:
                    sleep(sleep_time)
            if not quiet:
                raise RetryAPIException(e)

        return retry

    return decorator
