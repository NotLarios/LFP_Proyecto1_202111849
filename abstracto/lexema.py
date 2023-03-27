from abstracto.abstract import expression

class lexem(expression):
    def __init__(self, lexema, row, column):
        self.lexema = lexema
        super().__init__(row, column)

    def evaluate(self, node):
        return self.lexema

    def get_row(self):
        return super().get_row()
    
    def get_column(self):
        return super().get_column()