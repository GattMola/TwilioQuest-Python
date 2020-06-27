import sys

inputs = sys.argv
inputs.pop(0)

for num in sys.argv:
    int_num = int(num)
    if int_num % 3 == 0 and int_num % 5 == 0:
        print('fizzbuzz')
    elif int_num % 5 == 0:
        print('buzz')
    elif int_num % 3 == 0:
        print('fizz')
    else:
        print(int_num)
