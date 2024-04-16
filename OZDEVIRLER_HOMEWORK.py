class MathExpressionRecognizer:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
        self.valid_chars = set('+-*/()0123456789 ')
        self.steps = []

    def is_valid_expression(self, expression):
        expression = ''.join(filter(self.is_valid_char, expression))
        try:
            result = eval(expression)
            self.steps.append(f"'{expression}' ifadesinin değeri: {result}")
            return True
        except ZeroDivisionError:
            self.steps.append(f"'{expression}' ifadesi sıfıra bölme hatası verdi.")
            return False
        except SyntaxError:
            self.steps.append(f"'{expression}' ifadesi sözdizimi hatası verdi.")
            return False

    def is_valid_char(self, char):
        return char in self.valid_chars

if __name__ == "__main__":
    recognizer = MathExpressionRecognizer()

    while True:
        expr = input("Matematiksel ifadeyi girin (çıkmak için q): ")
        if expr.lower() == 'q':
            break

        recognizer.steps = []
        result = "matematiksel bir ifadedir" if recognizer.is_valid_expression(expr) else "matematiksel bir ifade değil"
        print(f"Girilen ifade '{expr}' -> {result}.")
        for step in recognizer.steps:
            print(step)
        print()