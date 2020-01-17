class OldDog():
    def __init__(self):
        print('I am an old dog !')
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('I eat it !')
            self.hungry = False
        else:
            print('No thanks!')


class NewDog(OldDog):
    def __init__(self):
        super().__init__()
        print('I am a new dog!')


olddog = OldDog()
olddog.eat()
olddog.eat()
newdog = NewDog()
newdog.eat()
newdog.eat()
