def safe_print_division(a, b):
    """Print a function that divides 2 integers and its result"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)