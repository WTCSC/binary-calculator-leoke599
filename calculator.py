def binary_calculator(bin1, bin2, operator):
    # error checks
    if any(c.isalpha() for c in bin1) == True:
        return 'Error'
    elif any(c.isalpha() for c in bin2) == True:
        return 'Error'
    for i in bin1:
        if i != '1':
            if i != '0':
                return 'Error' 
    for i in bin2:
        if i != '1':
            if i != '0':
                return 'Error'
    # conversion to decimal
    num = 0
    num2 = 2
    bin1 = list(bin1)
    bin2 = list(bin2)
    numbers = []
    numbers2 = []
    while num < 8:
        if bin1[num] == '1':
            bin1[num] = (256 / num2)
        if bin2[num] == '1':
            bin2[num] = (256 / num2)
        sum1 = numbers.append(bin2[num])
        sum2 = numbers2.append(bin1[num])
        num += 1
        num2 *= 2

    sum1 = sum([i for i in numbers if i != '0'])
    sum2 = sum([i for i in numbers2 if i != '0'])
    # overflow check
    total = sum1 + sum2
    if total >= 256:
        return 'Overflow'


    


