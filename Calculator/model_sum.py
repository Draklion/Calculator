def Sum(summand_1, summand_2, summand_3, summand_4, key):
    dictionary = {
        1: f"{summand_1+summand_2}",
        2: f"{complex(summand_1,summand_2)+complex(summand_3, summand_4)}".replace('(', '').replace(')', '')
    }
    return dictionary[key]
