from operaciones.arith import *
from operaciones.trigono import *
from abstracto.lexema import *
from abstracto.numbers import *
from abstracto.errores import error

palabras_reservadas = {
    'Reser_OPERACION':      'Operacion',
    'Reser_Valor1':         'Valor1',
    'Reser_Valor2':         'Valor2'   ,
    'Reser_Suma':           'Suma',
    'Reser_Resta':          'Resta',
    'Reser_Multiplicacion': 'Multiplicacion',
    'Reser_Division':       'Division',
    'Reser_Potencia':       'Potencia',
    'Reser_Raiz':           'Raiz',
    'Reser_Inverso':        'Inverso',
    'Reser_Seno':           'Seno',
    'Reser_Coseno':         'Coseno',
    'Reser_Tangente':       'Tangente',
    'Reser_Modulo':         'Mod',  
    'Reser_Texto':          'Texto',
    'Reser_ColFondoNodo':   'Color-Fondo-Nodo',
    'Reser_ColFuenteNodo':  'Color-Fuente-Nodo',
    'Reser_NodeShape':      'Forma-Nodo',
    'Coma':                 ',',
    'Punto':                '.',
    'DosPuntos':            ':',
    'CorcheteIzquierdo':    '[',
    'CorcheteDerecho':      ']',
    'LlaveIzquierda':       '{',
    'LlaveDerecha':         '}',
}

lexemas = list(palabras_reservadas.values())

global  n_linea
global  n_columna
global  instrucciones
global  lista_lexemas
global lista_errores
global contx

contx = 0
n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []

def instruccion(cadena):
    global  n_linea
    global  n_columna
    global  lista_lexemas

    lexema = ''
    pointer = 0

    while cadena:
        char = cadena[pointer]
        pointer += 1

        if char == '\"':
            lexema, cadena = armar_lexema(cadena[pointer:])
            if lexema and cadena:
                n_columna +=1
                l = lexem(lexema, n_linea, n_columna)
                lista_lexemas.append(l)
                n_columna += len(lexema)+1
                pointer = 0

        elif char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna +=1
                n = numbers(token, n_linea, n_columna) 
                lista_lexemas.append(n)
                n_columna += len(str(token)) +1
                pointer = 0

        elif char == '[' or char == ']':
            c = lexem(char, n_linea, n_columna)
            lista_lexemas.append(c)
            cadena = cadena[1:]
            pointer = 0
            n_columna +=1

        elif char == '\t':
            n_columna +=4
            cadena = cadena[1:]
            pointer = 0

        elif char == '\n':
            cadena = cadena[1:]
            pointer = 0
            n_linea += 1
            n_columna = 1

        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char ==':':
            n_columna += 1
            cadena = cadena[1:]
            pointer = 0
        else:
            lista_errores.append(error(char, n_linea, n_columna))
            cadena = cadena[1:]
            pointer = 0
            n_columna +=1
    
    return lista_lexemas


def armar_lexema(cadena):
    global  n_linea
    global  n_columna
    global  lista_lexemas

    lexema = ''
    pointer = ''

    for char in cadena:
        pointer += char
        if char == '\"':
            return lexema, cadena[len(pointer):]
        else:
            lexema += char
    return None, None

def armar_numero(cadena):
    numero = ''
    pointer = ''
    is_decimal = False

    for char in cadena:
        pointer += char
        if char == '.':
            is_decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t':
            if is_decimal:
                return float(numero), cadena[len(pointer)-1:]
            else:
                return int(numero), cadena[len(pointer)-1:]
        else:
            numero += char
    return None, None

def evaluate():
    global  instrucciones
    global  lista_lexemas

    operacion = ''
    n1 = ''
    n2 = ''

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.evaluate(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.evaluate(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.evaluate(None) == '[':
                n1 = evaluate()
        elif lexema.evaluate(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.evaluate(None) == '[':
                n2 = evaluate()
        
        if operacion and n1 and n2:
            return arith(n1, n2, operacion,
                              f'Inicio: {operacion.get_row()}: {operacion.get_column()}', 
                              f'Fin: {n2.get_row()}:{n2.get_column()}')
        
        elif operacion and n1 and operacion.evaluate(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return trigono(n1, operacion, 
                                   f'Inicio: {operacion.get_row()}: {operacion.get_column()}', 
                                   f'Fin: {n1.get_row()}:{n1.get_column()}')

    return None

def evaluate_():
    global instrucciones
    while True:
        operacion = evaluate()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    return instrucciones

def getErrores():
    global lista_errores
    return lista_errores