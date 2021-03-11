finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    min = 0
    max = len(array)-1
    guess = (min+max)//2

    while min <= max:
        if array[guess] == target :
            return True
        elif array[guess] < target :
            min = min+1
        else :
            max = min-1
        guess = (min+max)//2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)