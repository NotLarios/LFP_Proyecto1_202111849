from abstracto.abstract import expression

class numbers(expression):
    def __init__(self, num, row, column):
        self.num = num
        super().__init__(row, column)

    def evaluate(self, node):
        return self.num

    def get_row(self):
        return super().get_row()
    
    def get_column(self):
        return super().get_column()