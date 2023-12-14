def is_kind_of_class(obj, a_class):
    """
    Function that returs True: 
    - if the object is an instance of the specified class.
    - if the object is an instance of a class that inherited from that specified class.

    Otherwise False.

    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False