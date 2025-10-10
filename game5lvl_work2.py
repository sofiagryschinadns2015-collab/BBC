class TextGame:
    def __init__(self):
        self.level = 1
        self.texts = {
            1: "Привет МИР",
            2: "Ботать круто!",
            3: "1,2,3,4,5",
            4: "1234#",
            5: "Python - Awesome"
        }
    
    def start(self):
        print("Добро пожаловать в текстовую игру! ")
        print("=" * 50)
        
        while self.level <= 5:
            print(f"\n Уровень {self.level}")
            print("=" * 30)
            
            if self.level == 1:
                self.level_1()
            elif self.level == 2:
                self.level_2()
            elif self.level == 3:
                self.level_3()
            elif self.level == 4:
                self.level_4()
            elif self.level == 5:
                self.level_5()
            
            if self.level <= 4:
                continue_game = input("\nХотите перейти на следующий уровень? (да/нет): ").lower()
                if continue_game == 'да':
                    self.level += 1
                else:
                    print("Игра завершена!")
                    break
        else:
            print("\n🎉 Поздравляем! Вы прошли все уровни игры! 🎉")
    
    def level_1(self):
        text = self.texts[1]
        print(f"Текст: '{text}'")
        print("\nВыберите операцию:")
        print("1 - upper() - преобразовать в верхний регистр")
        print("2 - lower() - преобразовать в нижний регистр")
        print("3 - capitalize() - сделать первую букву заглавной")
        
        choice = input("Ваш выбор (1-3): ")
        
        if choice == '1':
            result = text.upper()
            print(f"Результат: {result}")
        elif choice == '2':
            result = text.lower()
            print(f"Результат: {result}")
        elif choice == '3':
            result = text.capitalize()
            print(f"Результат: {result}")
        else:
            print("Неверный выбор!")
    
    def level_2(self):
        text = self.texts[2]
        print(f"Текст: '{text}'")
        print("\nВыберите операцию:")
        print("1 - find() - найти позицию подстроки")
        print("2 - replace() - заменить подстроку")
        print("3 - index() - найти индекс символа")
        print("4 - count() - посчитать количество символов")
        
        choice = input("Ваш выбор (1-4): ")
        
        if choice == '1':
            substring = input("Введите подстроку для поиска: ")
            result = text.find(substring)
            if result != -1:
                print(f"Подстрока '{substring}' найдена на позиции: {result}")
            else:
                print(f"Подстрока '{substring}' не найдена")
                
        elif choice == '2':
            old_sub = input("Введите подстроку для замены: ")
            new_sub = input("Введите новую подстроку: ")
            result = text.replace(old_sub, new_sub)
            print(f"Результат: {result}")
            
        elif choice == '3':
            char = input("Введите символ для поиска: ")
            try:
                result = text.index(char)
                print(f"Символ '{char}' найден на позиции: {result}")
            except ValueError:
                print(f"Символ '{char}' не найден")
                
        elif choice == '4':
            char = input("Введите символ для подсчета: ")
            result = text.count(char)
            print(f"Символ '{char}' встречается {result} раз(а)")
        else:
            print("Неверный выбор!")
    
    def level_3(self):
        text = self.texts[3]
        print(f"Текст: '{text}'")
        print("\nВыберите операцию:")
        print("1 - split() - разделить строку")
        print("2 - join() - объединить с разделителем")
        
        choice = input("Ваш выбор (1-2): ")
        
        if choice == '1':
            delimiter = input("Введите разделитель (по умолчанию ','): ") or ","
            result = text.split(delimiter)
            print(f"Результат: {result}")
            
        elif choice == '2':
            delimiter = input("Введите разделитель для объединения: ")
            result = delimiter.join(text)
            print(f"Результат: {result}")
        else:
            print("Неверный выбор!")
    
    def level_4(self):
        text_a = self.texts[4]
        text_b = self.texts[5]
        
        print(f"Текст A: '{text_a}'")
        print(f"Текст B: '{text_b}'")
        
        print("\nВыберите операцию:")
        print("1 - isalpha() - проверка на буквы")
        print("2 - isdigit() - проверка на цифры")
        print("3 - strip() - удаление пробелов")
        print("4 - format() - форматирование строки")
        
        choice = input("Ваш выбор (1-4): ")
        
        if choice == '1':
            print(f"Текст A isalpha(): {text_a.isalpha()}")
            print(f"Текст B isalpha(): {text_b.isalpha()}")
            
        elif choice == '2':
            print(f"Текст A isdigit(): {text_a.isdigit()}")
            print(f"Текст B isdigit(): {text_b.isdigit()}")
            
        elif choice == '3':
            # Добавим пробелы для демонстрации
            text_with_spaces = "   " + text_a + "   "
            print(f"Текст с пробелами: '{text_with_spaces}'")
            print(f"После strip(): '{text_with_spaces.strip()}'")
            
        elif choice == '4':
            name = input("Введите ваше имя: ")
            age = input("Введите ваш возраст: ")
            result = "Привет, {}! Тебе {} лет.".format(name, age)
            print(f"Результат format(): {result}")
        else:
            print("Неверный выбор!")

    def level_5(self):
        text = self.texts[5]
        print(f" ФИНАЛЬНЫЙ УРОВЕНЬ!")
        print(f"Текст: '{text}'")
        print("\nВыберите любую операцию из всех уровней:")
        print("=" * 40)
        print("1 - upper() - преобразовать в верхний регистр")
        print("2 - lower() - преобразовать в нижний регистр")
        print("3 - capitalize() - сделать первую букву заглавной")
        print("4 - find() - найти позицию подстроки")
        print("5 - replace() - заменить подстроку")
        print("6 - index() - найти индекс символа")
        print("7 - count() - посчитать количество символов")
        print("8 - split() - разделить строку")
        print("9 - join() - объединить с разделителем")
        print("10 - isalpha() - проверка на буквы")
        print("11 - isdigit() - проверка на цифры")
        print("12 - strip() - удаление пробелов")
        print("13 - format() - форматирование строки")
        print("14 - title() - сделать каждое слово с заглавной буквы")
        print("15 - swapcase() - поменять регистр")
        
        choice = input("Ваш выбор (1-15): ")
        
        if choice == '1':
            result = text.upper()
            print(f"upper(): {result}")
            
        elif choice == '2':
            result = text.lower()
            print(f"lower(): {result}")
            
        elif choice == '3':
            result = text.capitalize()
            print(f"capitalize(): {result}")
            
        elif choice == '4':
            substring = input("Введите подстроку для поиска: ")
            result = text.find(substring)
            if result != -1:
                print(f"find('{substring}'): найдена на позиции {result}")
            else:
                print(f"find('{substring}'): не найдена")
                
        elif choice == '5':
            old_sub = input("Введите подстроку для замены: ")
            new_sub = input("Введите новую подстроку: ")
            result = text.replace(old_sub, new_sub)
            print(f"replace('{old_sub}', '{new_sub}'): {result}")
            
        elif choice == '6':
            char = input("Введите символ для поиска: ")
            try:
                result = text.index(char)
                print(f"index('{char}'): найден на позиции {result}")
            except ValueError:
                print(f"index('{char}'): не найден")
                
        elif choice == '7':
            char = input("Введите символ для подсчета: ")
            result = text.count(char)
            print(f"count('{char}'): встречается {result} раз(а)")
            
        elif choice == '8':
            delimiter = input("Введите разделитель (по умолчанию пробел): ") or " "
            result = text.split(delimiter)
            print(f"split('{delimiter}'): {result}")
            
        elif choice == '9':
            delimiter = input("Введите разделитель для объединения: ")
            result = delimiter.join(text)
            print(f"join('{delimiter}'): {result}")
            
        elif choice == '10':
            result = text.isalpha()
            print(f"isalpha(): {result}")
            
        elif choice == '11':
            result = text.isdigit()
            print(f"isdigit(): {result}")
            
        elif choice == '12':
            text_with_spaces = "   " + text + "   "
            print(f"Исходный текст с пробелами: '{text_with_spaces}'")
            result = text_with_spaces.strip()
            print(f"strip(): '{result}'")
            
        elif choice == '13':
            name = input("Введите ваше имя: ")
            skill = input("Введите ваш навык: ")
            result = "{} освоил {}!".format(name, skill)
            print(f"format(): {result}")
            
        elif choice == '14':
            result = text.title()
            print(f"title(): {result}")
            
        elif choice == '15':
            result = text.swapcase()
            print(f"swapcase(): {result}")
            
        else:
            print("Неверный выбор!")
            
        # Дополнительная информация о тексте
        print(f"\nДополнительная информация о тексте:")
        print(f"Длина текста: {len(text)} символов")
        print(f"Начинается с 'Python': {text.startswith('Python')}")
        print(f"Заканчивается на 'Awesome': {text.endswith('Awesome')}")


# Запуск игры
if __name__ == "__main__":
    game = TextGame()
    game.start()