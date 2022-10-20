def Subtraction(reduced1, deductible1, reduced2, deductible2, key):
    dictionary = {
        1: f"{reduced1-deductible1}",
        2: f"{complex(reduced1,deductible1)-complex(reduced2, deductible2)}".replace('(', '').replace(')', '')
    }
    return dictionary[key]
