bin1 = '11111111'
bin2 = '00000000'
op = "+"
num = 0
num2 = 2
bin1 = list(bin1)
bin2 = list(bin2)
numbers = []
numbers2 = []
binary = []
while num < 8:
    if bin1[num] == '1':
        bin1[num] = (256 / num2)
    if bin2[num] == '1':
        bin2[num] = (256 / num2)
    sum1 = numbers.append(bin1[num])
    sum2 = numbers2.append(bin2[num])
    num += 1
    num2 *= 2
print(numbers)
sum1 = sum([i for i in numbers if i != '0'])
sum2 = sum([i for i in numbers2 if i != '0'])
total = sum1 + sum2
print(total)
num1 = 0
while num1 < 8:
    if numbers[num1] == '0':
        numbers[num1] = '0'
    else:
        numbers[num1] = '1'
    bin = binary.append(numbers[num1])
    num1 += 1
print(bin)

