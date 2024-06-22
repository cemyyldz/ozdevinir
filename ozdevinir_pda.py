class MathExpressionRecognizerPDA:
    def __init__(self):
        # Operatörler, rakamlar ve geçerli karakterler kümesi tanımlanıyor
        self.operators = {'+', '-', '*', '/'}
        self.digits = set('0123456789')
        self.valid_chars = set('+-*/()0123456789 ')
        self.stack = []  # Yığıın başlangıçta boş olarak ayarlanıyor

    def recognize_expression(self, expression):
        current_state = 0  # PDA'nın başlangıç durumu
        index = 0  # İfadeyi karakter karakter taramak için kullanılacak index
        
        self.stack = []  # Yığıın, her yeni ifade için sıfırlanıyor
        
        # İfade boyunca tarama yapılıyor
        while index < len(expression):
            char = expression[index]  # İfadenin mevcut indeksindeki karakter alınıyor
            
            if char in self.valid_chars:
                if current_state == 0:
                    if char in self.digits:
                        current_state = 1  # Rakam okunmuşsa durum değiştiriliyor
                        index += 1
                    elif char == '(':
                        self.stack.append('(')  # Yığına '(' karakteri ekleniyor
                        index += 1
                    else:
                        return False  # Geçersiz karakter durumu
                elif current_state == 1:
                    if char in self.digits:
                        index += 1
                    elif char in self.operators:
                        current_state = 0  # Operatör okunduğunda durum değiştiriliyor
                        index += 1
                    elif char == ')':
                        if self.stack and self.stack[-1] == '(':
                            self.stack.pop()  # '(' karakteri varsa yığından çıkarılıyor
                            index += 1
                        else:
                            return False  # Parantez eşleşme hatası
                    elif char == ' ':
                        index += 1  # Boşluk karakteri atlanıyor
                    else:
                        return False  # Geçersiz karakter durumu
            else:
                return False  # Geçersiz karakter durumu
        
        # Tarama sonrası durum kontrolü yapılıyor
        if current_state == 1 and self.stack == []:
            return True  # Geçerli matematiksel ifade
        else:
            return False  # Geçersiz matematiksel ifade

if __name__ == "__main__":
    recognizer = MathExpressionRecognizerPDA()

    while True:
        expr = input("Matematiksel ifadeyi girin (çıkmak için q): ")
        if expr.lower() == 'q':
            break
        
        # İfadenin geçerliliği kontrol ediliyor
        result = "geçerli bir matematiksel ifade" if recognizer.recognize_expression(expr) else "geçersiz bir matematiksel ifade"
        print(f"Girilen ifade '{expr}' -> {result}.")
