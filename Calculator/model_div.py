def Division(divisible1, divider1, divisible2, divider2, key):
    dictionary = {
        1: f"{divisible1/divider1}",
        2: f"{divisible1%divider1}",
    }
    return dictionary[key]
