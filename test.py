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
import conversor
import unittest


class TestConversiones(unittest.TestCase):
    def test_binario_decimal(self):
        esperado = 7
        actual = conversiones.binario_a_decimal("111")
        self.assertEqual(actual, esperado)

    def test_decimal_binario(self):
        esperado = "111"
        actual = conversiones.decimal_a_binario(7)
        self.assertEqual(actual, esperado)

    def test_octal_decimal(self):
        esperado = 123
        actual = conversiones.octal_a_decimal("173")
        self.assertEqual(actual, esperado)

    def test_decimal_octal(self):
        esperado = "173"
        actual = conversiones.decimal_a_octal(123)
        self.assertEqual(actual, esperado)

    def test_hexadecimal_decimal(self):
        esperado = 255
        actual = conversiones.hexadecimal_a_decimal("ff")
        self.assertEqual(actual, esperado)

    def test_decimal_hexadecimal(self):
        esperado = "ff"
        actual = conversiones.decimal_a_hexadecimal(255)
        self.assertEqual(actual, esperado)

    def test_obtener_numero_decimal(self):
        valores = [
            {
                "base": "2",
                "numero": "111",
                "esperado": 7,
            },
            {
                "base": "8",
                "numero": "173",
                "esperado": 123,
            },
            {
                "base": "16",
                "numero": "f",
                "esperado": 15,
            },
        ]
        for valor in valores:
            esperado = valor["esperado"]
            actual = conversor.obtener_numero_decimal(
                valor["base"], valor["numero"])
            self.assertEqual(actual, esperado)


if __name__ == "__main__":
    unittest.main()
