from inspect import stack
from os.path import split


def get_scope() -> str:
    return split(stack()[-1].filename)[-1] + ":" + str(stack()[-1].lineno)
