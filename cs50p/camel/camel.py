camel = input("camelCase: ")


def snake(camel):
    return ''.join([i if not i.isupper() else "_" + i.lower() for i in camel]).lstrip("_")


print("snake_case: " + snake(camel))
