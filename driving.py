print('welcome to parivahan')
print('enter your age')

age=int(input())



if 7<age<18:
    print('you cannot drive')
if age==18:
    print('your can apply for driving licence')
elif 18<age<101:
    print('you can drive')
else:
    print('you have entered wrong age')