def no_c(my_string):
    """Remove all characters c and C from a string"""
    message = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(message))
