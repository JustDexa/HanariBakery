from abc import ABC, abstractmethod

class Topping(ABC):
    @abstractmethod
    def tambah_topping(self):
        pass
