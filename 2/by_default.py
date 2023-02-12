# работа с функциями по умолчанию

# def new_string(symbol, count):
    # return symbol*count


# print(new_string('!', 5))   # получим !!!!!
# print(new_string('!'))        # TypeError:

def new_string(symbol, count=3): # если укажем в аргументе =3
    return symbol*count

print(new_string('!'))       #  то получим !!!
print(new_string('4'))       # 444
print(new_string(4))         # 12