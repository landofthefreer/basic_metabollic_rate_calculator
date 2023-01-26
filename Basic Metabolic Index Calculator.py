name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

#BMI = (weight in pounds x 703) / (height in inches x height in inches)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name +", you are underweight. ")
    elif (BMI <= 24.9):
        print(name +", you are normal weight.")
    elif (BMI < 29.9):
        print(name +", you are overweight.")
    elif (BMI < 34.9):
        print(name +", you are obese.")
    elif (BMI < 39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input.")

#Enter your name: Luis
#Enter your weight in pounds: 132
#Enter your height in inches: 66
#21.303030303030305
#Luis, you are normal weight.
