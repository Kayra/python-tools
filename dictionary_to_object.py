

class ObjectFromDictionary:
    """
    Transform a dictionary into an object for easier use.
    """
    def __init__(self, dictionary):
        self.__dict__ = dictionary


class DictionaryObjectFromDictionary(dict):
    """
    Transform a dictionary into an object but keep dictionary attribute methods.
    """
    def __getattr__(self, attribute_name):
        if attribute_name in self:
            return self[attribute_name]
        else:
            raise AttributeError("No such attribute: " + attribute_name)

    def __setattr__(self, attribute_name, value):
        self[attribute_name] = value

    def __delattr__(self, attribute_name):
        if attribute_name in self:
            del self[attribute_name]
        else:
            raise AttributeError("No such attribute: " + attribute_name)
