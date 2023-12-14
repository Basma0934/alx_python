def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class.
    Check if the object is an instance of a class that inherited from that specified class

    """
    if isinstance(obj, a_class):
        return True
    return False