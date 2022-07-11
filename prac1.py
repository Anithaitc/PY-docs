#simple_interest
def calculate_simple_interest(principal,interest,duration):
    return principal*(1+interest*0.01*duration)
print(calculate_simple_interest(2500,5,5))
#another one
def caluculate_amount(principal,interest,duration):
    total_interest=interest*0.1*duration*principal
    total_amount=principal+total_interest
    return total_amount
print(caluculate_amount(2500,5,5))
#example
numbers=[1,2,3,4]
for number in numbers:
    print(number)
for index,number in enumerate(numbers):
    print(f'{index}-{number}')
