from abstracto.abstract import expression

class arith(expression):
    def __init__(self, left, right, type, row, column):
        self.left = left
        self.right = right
        self.type = type
        super().__init__(row, column)

    def evaluate(self, node):
        left_num = ''
        right_num = ''

        if self.left is not None:
            left_num = self.left.evaluate(None)
        if self.right is not None:
            right_num = self.right.evaluate(None)

        if self.type.evaluate(node) == 'Suma':
            return float(left_num) + float(right_num)
        
        elif self.type.evaluate(node) == 'Resta':
            return float(left_num) - float(right_num)
        
        elif self.type.evaluate(node) == 'Multiplicacion':
            return float(left_num) * float(right_num)
        
        elif self.type.evaluate(node) == 'Division':
            return float(left_num) / float(right_num)
        
        elif self.type.evaluate(node) == 'Modulo':
            return float(left_num) % float(right_num)
        
        elif self.type.evaluate(node) == 'Potencia':
            return float(left_num) ** float(right_num)
        
        elif self.type.evaluate(node) == 'Raiz':
            return float(left_num) ** (1/float(right_num))
        
        elif self.type.evaluate(node) == 'Inverso':
            return float(left_num) ** -1
        else:
            return None
        
    def get_row(self):
        return super().get_row()
    
    def get_column(self):
        return super().get_column()