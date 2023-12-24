def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""

    if a_class == object:
#         return False
#     elif type(obj) == bool:
#         return False
#     else:
#         class_name = type(obj)
#         if issubclass(class_name, a_class):
#             return True
#         else:
#             return False
        
        return type(obj) is a_class
