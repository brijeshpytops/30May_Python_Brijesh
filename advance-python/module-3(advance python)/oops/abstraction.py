from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class dog(animal):
    def voice(self):
        print("bark")

    
class cat(animal):
    def voice(self):
        print("meow")

obj = dog()
obj.voice()

obj = cat()
obj.voice()