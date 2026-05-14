'''Class Deep

(1) Encapsulation
(2) Inheritance
(3) Plimorphism
'''

print("===== Inheritance ========")
# Parent > Child


class Animal:

    description = "The class creates animals"

    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


class Dog(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        pass


class Fish(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()


dog.make_voice
cat.make_voice

print("===== Plimorphism ========")

dog.make_voice
fish.make_voice

# Fish >fish > Animal > object

a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
result = a and b and c
print(f"the result:{result} ")


# Fish > ANimal > objject

data1 = issubclass(Fish, Animal)
data2 = issubclass(Fish, Animal)
print("data:", data1, data2)
