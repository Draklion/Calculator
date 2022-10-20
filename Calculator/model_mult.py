def Multiplication(multiplier_1, multiplier_2, multiplier_3, multiplier_4, key):
    dictionary = {
        1: f"{multiplier_1*multiplier_2}",
        2: f"{complex(multiplier_1, multiplier_2)*complex(multiplier_3, multiplier_4)}".replace('(', '').replace(')', '')
    }
    return dictionary[key]
