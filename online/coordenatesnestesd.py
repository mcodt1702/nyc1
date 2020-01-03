def find_max(numbers):

    maxi = 0
    for number in numbers:
        if maxi < number:
            maxi = number
    return maxi


