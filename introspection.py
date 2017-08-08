
def discover_exception(function_to_test):

    try:
        function_to_test()
    except Exception as exception:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(exception).__name__, exception.args)
        print(message)
