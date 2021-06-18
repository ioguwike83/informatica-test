list_name = ["akhigbe", "mark", "jude"]


def Cap_name(object_list):
    for item in object_list:
        value = []
        value.append(item.upper())
        return value


Cap_name(list_name)

# list compre...
ls = [item.upper() for item in list_name]
    