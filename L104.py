#Amanda Miloserny and Cathy Doherty
redvelvet = {"chocolate": 1, "flour": 2, "egg": 3, "sugar": 4, "butter": 5}
lemon = {"lemon": 1, "flour": 2, "egg": 3, "sugar": 4, "butter": 5}

def cakes():
    match = []
    x = redvelvet
    y = lemon
    for ingredient in x:
        if ingredient in y:
            match.append(ingredient)
    print(match)

cakes()
