import math
from abstracto.abstract import expression

class trigono(expression):
    def __init__(self, left, type, row, column):
        self.left = left
        self.type = type
        super().__init__(row, column)

    def evaluate(self, node):
        left_num = ''

        if self.left is not None:
            left_num = self.left.evaluate(None)
        
        if self.type.evaluate(node) == 'Seno':
            return math.sin(left_num)
        
        elif self.type.evaluate(node) == 'Coseno':
            return math.cos(left_num)
        
        elif self.type.evaluate(node) == 'Tangente':
            return math.tan(left_num)
        
        elif self.type.evaluate(node) == 'Cotangente':
            return 1/math.tan(left_num)
        
        elif self.type.evaluate(node) == 'Secante':
            return 1/math.cos(left_num)
        
        elif self.type.evaluate(node) == 'Cosecante':
            return 1/math.sin(left_num)
        
        else:
            return None 
        
    def get_row(self):
        return super().get_row()
    
    def get_column(self):
        return super().get_column()