file = open('input.txt', 'r')


# save all combinations in a list
# split each string in 2

list_of_combinations = []

for item in file:
    list_of_combinations.append(item.rstrip().split(": "))


#PART 1
def define_if_is_valid(element):
    #identify policy
        #split numbers and letter
    policy = element[0].split(" ")
        #identify min and max
    min_max = [int(i) for i in policy[0].split("-")]
    char = policy[1]

    password = element[1]
    validity = False
    count_in_password = password.count(char)
    if min_max[0] <= count_in_password <= min_max[1]:
        validity = True
    else:
        validity = False
    
    return validity
    

#print(define_if_is_valid(list_of_combinations[1]))


def count_valids(lista):
    count = 0
    for item in lista:
        if define_if_is_valid(item):
            count = count + 1
    print(count)

print("result Part 1")
count_valids(list_of_combinations)


#PART 2

def new_policy(element):
    policy = element[0].split(" ")
    #['x-y', 'C']
    min_max = [int(i) for i in policy[0].split("-")]
    p1 = min_max[0]
    p2 = min_max[1]

    char = policy[1]

    password = element[1]

    validity = False

    if password[p1-1] == char and password[p2-1] != char :
        validity = True
    if password[p1-1] != char and password[p2-1] == char :
        validity = True
    
    return validity

#print(new_policy(list_of_combinations[0]))

def count_valids_2(lista):
    count = 0
    for item in lista:
        if new_policy(item):
            count = count + 1
    print(count)

print("result Part 2")
count_valids_2(list_of_combinations)