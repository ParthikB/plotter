def add_wrapper(item):
    def wrap():
        return f"Wrapped {item()}"
    return wrap


@add_wrapper
def laptop():
    return "a brand new laptop!\n"


print(laptop())