class Calculator:
    def __init__(self):
        self.history = []  # Хранит историю операций
        self.last_result = 0  # Хранит последний результат
    
    def add(self, num1, num2):
        result = num1 + num2
        self.last_result = result
        self.history.append(f"{num1} + {num2} = {result}")
        return result
        
    def subtract(self, num1, num2):
        result = num1 - num2
        self.last_result = result
        self.history.append(f"{num1} - {num2} = {result}")
        return result
        
    def multiply(self, num1, num2):
        result = num1 * num2
        self.last_result = result
        self.history.append(f"{num1} * {num2} = {result}")
        return result
        
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно")
        result = num1 / num2
        self.last_result = result
        self.history.append(f"{num1} / {num2} = {result}")
        return result

# Добавляем интерфейс для работы с калькулятором
def main():
    calc = Calculator()
    
    while True:
        print("\nКалькулятор")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. История")
        print("6. Выход")
        
        choice = input("Выберите операцию (1-6): ")
        
        if choice == '6':
            break
        elif choice == '5':
            if calc.history:
                print("\nИстория операций:")
                for operation in calc.history:
                    print(operation)
            else:
                print("История пуста")
            continue
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                
                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"Результат: {result}")
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"Результат: {result}")
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"Результат: {result}")
                elif choice == '4':
                    try:
                        result = calc.divide(num1, num2)
                        print(f"Результат: {result}")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: введите корректные числа")
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()class Calculator:
    def __init__(self):
        self.history = []  # Хранит историю операций
        self.last_result = 0  # Хранит последний результат
    
    def add(self, num1, num2):
        result = num1 + num2
        self.last_result = result
        self.history.append(f"{num1} + {num2} = {result}")
        return result
        
    def subtract(self, num1, num2):
        result = num1 - num2
        self.last_result = result
        self.history.append(f"{num1} - {num2} = {result}")
        return result
        
    def multiply(self, num1, num2):
        result = num1 * num2
        self.last_result = result
        self.history.append(f"{num1} * {num2} = {result}")
        return result
        
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно")
        result = num1 / num2
        self.last_result = result
        self.history.append(f"{num1} / {num2} = {result}")
        return result

# Добавляем интерфейс для работы с калькулятором
def main():
    calc = Calculator()
    
    while True:
        print("\nКалькулятор")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. История")
        print("6. Выход")
        
        choice = input("Выберите операцию (1-6): ")
        
        if choice == '6':
            break
        elif choice == '5':
            if calc.history:
                print("\nИстория операций:")
                for operation in calc.history:
                    print(operation)
            else:
                print("История пуста")
            continue
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                
                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"Результат: {result}")
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"Результат: {result}")
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"Результат: {result}")
                elif choice == '4':
                    try:
                        result = calc.divide(num1, num2)
                        print(f"Результат: {result}")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: введите корректные числа")
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()