#Amanda Miloserny and Cathy Doherty
def my_get_method(k, d, default):
    if k in d:
        return d[k]
    else:
        return default

d = {"gold":1, "silver":2, "copper":3}

print(my_get_method("silver", d, 9))

print(my_get_method("iron",d,9))

print(my_get_method(True, d, 9))
