def sum(nubmer_one,number_two):
    nubmer_one_int = convert_integer(nubmer_one)
    number_two_int = convert_integer(number_two)

    result = nubmer_one_int + number_two_int

    return result

def convert_integer(number_string):

    convert_integer = int(number_string)
    return convert_integer

answer = sum("1","2")