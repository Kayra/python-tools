
def function_to_test():
    pass

try:
    function_to_test()
except Exception as ex:
    template = "An exception of type {0} occured. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
