
def balancear_parentesis(funcion):
    paren_abiertos = 0
    paren_cerrados = 0
    
    for char in funcion:
        if char == '(':
            paren_abiertos += 1
        elif char == ')':
            if paren_abiertos > paren_cerrados:
                paren_cerrados += 1
            else:
                # Si hay más cerrados que abiertos, ignoramos este paréntesis
                funcion = funcion.replace(')', '', 1)
    
    # Añadir paréntesis faltantes al final
    funcion += ')' * (paren_abiertos - paren_cerrados)
    
    return funcion

def verificar_y_corregir_sintaxis(funcion):
    funcion_corregida = balancear_parentesis(funcion)
    if funcion != funcion_corregida:
        return funcion_corregida, "Se han añadido o eliminado paréntesis para balancear la expresión."
    return funcion, None