def Division(divisible1, divider1, divisible2, divider2, key):
    try:
        divisible1/divider1
    except ZeroDivisionError:
        key = 4
    dictionary = {
        1: f"{divisible1/divider1}",
        # 2: f"{complex(divisible1, divider1)/complex(divisible2, divider2)}".replace('(', '').replace(')', ''),
        3: f"{divisible1%divider1}",
        4: "0"
    }
    return dictionary[key]
