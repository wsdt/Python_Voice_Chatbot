""" Converts a dictionary to a list by only adding
the keys of the dict to the list. """
def dict2listByKey(dict):
    list = []
    for key in dict:
        list.append(key)
    return list