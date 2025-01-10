import math
import operator
# sets up conversion from string opertors to real operators
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}
def binary_calculator(bin1, bin2, op):
    # error checks
    for i in bin1:
        if i != '1' and i != '0':
            return 'Error' 
    for i in bin2:
        if i != '1' and i != '0':
            return 'Error'
    # conversion to decimal
    index = 0
    divider = 2
    bin1 = list(bin1)
    bin2 = list(bin2)
    numbers = []
    numbers2 = []
    binary = []
    # iterates through every index of the binary numbers and assigns them their decimal number
    while index < len(bin1):
        if bin1[index] == '1':
            bin1[index] = (256 / divider)
        if bin2[index] == '1':
            bin2[index] = (256 / divider)
        sum1 = numbers.append(bin1[index])
        sum2 = numbers2.append(bin2[index])
        index += 1
        divider *= 2
    # gets the sum of each binary number
    sum1 = sum([i for i in numbers if i != '0'])
    sum2 = sum([i for i in numbers2 if i != '0'])
    # checks if binaries or dividing by 0 and returns NaN if so
    if op == "/":
        if sum2 == 0:
            return 'NaN'
        if sum1 == 0:
            return 'NaN'
    # gets the total of the two sums using ops[op] to convert the string to an actual operator
    total = ops[op](sum1, sum2)
    total = math.floor(total)
    # checks if the total is in the negatives to return Overflow
    if total < 0:
        return "Overflow"
    # inserts either 0 or 1 into a list until the total reaches zero. will give 0 if the number divides evenly and gives 1 if the divided number gives a remainder
    while total > 0:
        binary.insert(0, str(total % 2))
        total = int(total / 2)
    # inserts additional 0s if the binary number is not 8 characters
    if len(binary) <= 7:
        while len(binary) <= 7:
            binary.insert(0, '0')
    # checks if there are more than 8 character and if there is will return Overflow
    if len(binary) > 8:
        return 'Overflow'
    return "".join(binary)


    


