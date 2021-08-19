class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    exceptionList = []
    newExcept = None
    for func in func_ls:
        try:
            func()
        except Exception as e:
            newExcept = ExceptionProxy(str(e), func)
        else:
            newExcept = ExceptionProxy("ok!", func)
        finally:
            exceptionList.append(newExcept)
    return exceptionList
