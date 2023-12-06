def multiply_list_map(my_list=[], number=0):
    """Returning a list with all values multiplied by a number without using any loops."""
    return (list(map(lambda x: x*number, my_list)))