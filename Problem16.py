#16.You are given a large integer represented as an integer array digits, where each digits[i] is the i digit of the integer.The digits are ordered from most significant to least significant in left to right order.The large integer does not contain any leading 0's.
def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # if all digits were 9
    return [1] + digits