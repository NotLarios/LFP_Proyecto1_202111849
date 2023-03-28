from abc import ABC, abstractmethod

class expression(ABC):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    #Método abstracto para calcular
    @abstractmethod
    def evaluate(self, node):
        pass

    @abstractmethod
    def get_row(self):
        return self.row
    
    @abstractmethod
    def get_column(self):
        return self.column