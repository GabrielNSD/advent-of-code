file = open('input.txt', 'r')

#find two entries that sum 2020

fs= []
for item in file:
    fs.append(int(item))


def find_numbers(lista):
    for item in fs:
        for item_again in fs:
            result = item+item_again
            if result == 2020:
                return [item, item_again]


#multiply entries
def multiply_numbers(lista):
    result = 1
    for item in lista:
        result = result * item
    return result

print('result part 1: ')
print(multiply_numbers(find_numbers(fs)))



#PART 2

#find 3 entries that sum 2020

def find_three_numbers(lista):
    for item in fs:
        for item_again in fs:
            result1 = item+item_again
            if result1 < 2020 :
                for item_again_again in fs:
                    result2 = item + item_again +item_again_again
                    if result2 == 2020:
                        return [item, item_again,item_again_again]

print('result part 2: ')
print(multiply_numbers(find_three_numbers(fs)))