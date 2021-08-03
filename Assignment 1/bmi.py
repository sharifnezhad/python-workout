weight=float(input('Enter your weight (kg):'))
height=float(input('Enter your height (m)'))
bmi=weight/(height**2)
if bmi<18.5:
    print('youre in the underweight range')
elif bmi>=18.5 and bmi<=24.9:
    print('youre in the healthy weight range')
elif bmi>=25 and bmi<=29.9:
    print('youre in the overweight range')
elif bmi>=30 and bmi<=34.9:
    print('youre in the obese range')
elif bmi<=35:
    print('You are very fat')