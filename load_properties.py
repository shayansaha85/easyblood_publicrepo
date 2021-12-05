from jproperties import Properties


def load_properties():
    configs = Properties()
    with open('database.properties', 'rb') as read_prop:
        configs.load(read_prop)
        
    return configs