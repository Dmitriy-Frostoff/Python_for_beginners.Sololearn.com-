weight=int(input("вес в кг "))
height=float(input("рост в м "))
a=weight/(height**2)
if a < 18.5:
    print("Underweight")
if (a >= 18.5) and (a < 25 ):
    print("Normal")
if (a>25) and (a < 30):
    print("Overweight")
if (a>30):
    print("Obesity")
