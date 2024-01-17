class Bird():
    isBird = True

class Mammal():
    isMammal = True

class Bat(Bird, Mammal):
    pass

bat = Bat()
print(bat.isBird)
print(bat.isMammal)
