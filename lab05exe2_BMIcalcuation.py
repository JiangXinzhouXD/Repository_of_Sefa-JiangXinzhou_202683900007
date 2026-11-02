def weight_seek():
    weight_of_user=float(input('Your weight is PS in kg'))
    return weight_of_user


def height_seek():
    height_of_user=float(input("Your height is PS in m"))
    return height_of_user


def BMI_calculation(weight_of_user,height_of_user):
    BMI=weight_of_user/(height_of_user**2)
    print('Your BMI is',BMI)
    return BMI


def assessment(BMI):
    if BMI<=18.5:
        print('underweight')
    elif BMI<=24.9:
        print('Normal weight')
    elif BMI<=29.9:
        print('Overweight')
    else:
        print('Obese')


w=weight_seek()
h=height_seek()
BMI=BMI_calculation(w,h)
assessment(BMI)
