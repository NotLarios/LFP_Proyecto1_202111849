from abstracto.abstract import expression

class error(expression):
    def __init__(self, lexema, row, column):
        self.lexema = lexema
        super().__init__(row, column)

    def evaluate(self, number):
        num = f'\t\t"No.": {number}\n'
        desc = '\t\t"Descripcion-Token": {\n'
        lexem = f'\t\t\t"Lexema": {self.lexema}\n'
        type = f'\t\t\t"Tipo": Error Lexico\n'
        row = f'\t\t\t"Fila": {self.row}\n'
        column = f'\t\t\t"Columna": {self.column}\n'
        end = '\t\t}\n'

        return '\t{\n' + num + desc + lexem + type + row + column + end +'\t}'
    
    def get_row(self):
        return super().get_row
    
    def get_column(self):
        return super().get_column