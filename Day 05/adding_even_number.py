# Range function with for loop
# for numbers in range(1, 21): # doesn't include the number 21, only functions within 1-20
#     print(numbers)
# for numbers in range(1, 11, 3): #stepping: means that the number at the third position is used for stepping. the range from 1 - 11 is printed in addition of 3 after each nuumber. example 1, 1+3 = 4, 4+3 = 7, 7+3 = 10. the output will be 1, 4, 7 and 10
    # print(numbers)

#Gauss Challenge
sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(sum)