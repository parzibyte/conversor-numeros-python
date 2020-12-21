"""

  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
____________________________________
/ Si necesitas ayuda, contáctame en \
\ https://parzibyte.me               /
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Creado por Parzibyte (https://parzibyte.me).
------------------------------------------------------------------------------------------------
Si el código es útil para ti, puedes agradecerme siguiéndome: https://parzibyte.me/blog/sigueme/
Y compartiendo mi blog con tus amigos
También tengo canal de YouTube: https://www.youtube.com/channel/UCroP4BTWjfM0CkGB6AFUoBg?sub_confirmation=1
------------------------------------------------------------------------------------------------
"""
import conversiones


# Si todo va bien, regresa una tupla con la base de origen, el número a convertir y la base de destino
def solicitar_datos_a_usuario():
    bases_soportadas = ["2", "8", "10", "16", ]
    base_origen = input("""
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
Elige la base desde donde conviertes: [2, 8, 10, 16]: """)
    if base_origen not in bases_soportadas:
        print("La base que ingresaste no está soportada")
        return
    numero = input(
        f"Ok, vas a convertir desde la base {base_origen}. Ingresa el número a convertir: ")
    base_destino = input("""
2 - Binario
8 - Octal
10 - Decimal
16 - Hexadecimal
Elige la base a la que conviertes: [2, 8, 10, 16]: """)
    if base_destino not in bases_soportadas:
        print("La base de destino no está soportada")
        return
    return (base_origen, numero, base_destino)


def obtener_numero_decimal(base_origen, numero):
    if base_origen == "2":
        return conversiones.binario_a_decimal(numero)
    elif base_origen == "8":
        return conversiones.octal_a_decimal(numero)
    elif base_origen == "10":
        return int(numero)
    elif base_origen == "16":
        return conversiones.hexadecimal_a_decimal(numero)


def convertir(numero, base_destino):
    if base_destino == "2":
        return conversiones.decimal_a_binario(numero)
    elif base_destino == "8":
        return conversiones.decimal_a_octal(numero)
    elif base_destino == "10":
        return int(numero)
    elif base_destino == "16":
        return conversiones.decimal_a_hexadecimal(numero)


if __name__ == '__main__':
    datos = solicitar_datos_a_usuario()
    # Comprobamos si los datos son correctos
    if datos:
        base_origen, numero, base_destino = datos
        # Para ahorrarnos código, vamos a convertir el número a decimal (sin importar la base de origen) y luego ese número
        # lo convertimos a la base de destino
        numero_decimal = obtener_numero_decimal(base_origen, numero)
        # Y a ese decimal lo convertimos a la base deseada
        resultado = convertir(numero_decimal, base_destino)
        print(resultado)
