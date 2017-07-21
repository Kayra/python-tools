

# Just for better way to reference
class ObjectFromDictionary:
    def __init__(self, dictionary):
        self.__dict__ = dictionary


# With dict methods
class objdict(dict):

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
