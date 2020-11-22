import unittest
import lab1
import sys
import os

class MyTestCase(unittest.TestCase):

#Тест проверки функции проверки правильного пути
    #Корректный путь
    def test_ErrorPath(self):
        self.assertEqual(lab1.ErrorPath('C:folder\folder2\file.txt'), 1)
    def test_ErrorPath(self):
        self.assertEqual(lab1.ErrorPath('C:folder\file.txt'), 1)
    def test_ErrorPath(self):
        self.assertEqual(lab1.ErrorPath('C:file.txt'), 1)
    #Некорректный путь
    def test_ErrorPath(self):
        self.assertEqual(lab1.ErrorPath('Cer\folder2\file.txt'), 0)
    #Пустая строка
    def test_ErrorPath(self):
        self.assertEqual(lab1.ErrorPath(''), 0)

# Тест проверки функции проверки корректности символа замены
    #Корректный символ
    def test_ErrorSymbol(self):
        self.assertEqual(lab1.ErrorSymbol('*'), 1)
    #Некорректный набор символов
    def test_ErrorSymbol(self):
        self.assertEqual(lab1.ErrorSymbol('*/*-+'), 0)
    #Пустая строка
    def test_ErrorSymbol(self):
        self.assertEqual(lab1.ErrorSymbol(''), 0)

# Тест функции замены слова на определение в словаре
    #Общие случаи
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('hello world','hello goodbye'),"goodbye world")
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('hello earth, hello mars, hello sun','hello goodbye\nsun moon'),"goodbye earth, goodbye mars, goodbye moon")
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('He who lived and thought cannot but despise people in his soul.', 'soul mind\ndespise love'), "He who lived and thought cannot but love people in his mind.")

    #Одно слово
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('hello world','hello goodbye'),"goodbye world")
    #Больше одного слова
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('hello hello hello hello world', 'hello goodbye'), "goodbye goodbye goodbye goodbye world")
    #Ни одного слова не соответствует
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('Privet mir','hello goodbye'),"Privet mir")
    #Пустая строка
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('','hello goodbye'),"")
    #Пустой словарь
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('hello world',''),"hello world")
    #Все слова соответствуют
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('hello hello hello hello', 'hello goodbye'), "goodbye goodbye goodbye goodbye")
    #Пустая строка, пустой словарь
    def test_Vocabulary(self):
        self.assertEqual(lab1.Vocabulary('',''),"")
    #Некорректный словарь
    def test_Vocabulary(self):
        with self.assertRaises(IndexError):
            lab1.Vocabulary('hello hello hello hello', 'hello')
    def test_Vocabulary(self):
        with self.assertRaises(IndexError):
            lab1.Vocabulary('hello hello hello hello', 'hello\ngoodbye')


# Тест функции замены слова на символ
    #Общие случаи
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('hello world', 'hello\ngoodbye','*'), "***** world")
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('hello earth, hello mars, hello sun', 'earth\nmars\nsun','*'), "hello *****, hello ****, hello ***")
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('He who lived and thought cannot but despise people in his soul.', 'who\nlived\nsoul','*'), "He *** ***** and thought cannot but despise people in his ****.")


    #Слово найдено и заменено на символы
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('hello world', 'hello\ngoodbye','*'), "***** world")
    # Слово не найдено
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('hello world', 'goodbye','*'), "hello world")
    #Найдено более одного слова
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('hello goodbye hello hello world', 'hello\ngoodbye','*'), "***** ******* ***** ***** world")
    # Пустая строка
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('', 'goodbye','*'), "")
    # Пустой словарь
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('hello world', '','*'), "hello world")
    # Пустой словарь и пустая строка
    def test_Сensorship(self):
        self.assertEqual(lab1.Сensorship('', '','*'), "")

#Аргументы командной строки
    def test_main(self):
        result = os.system('python3 lab1.py -t C:\\Users\\mshak_000\\Desktop\\ProgEnLab1\\text -r C:\\Users\\mshak_000\\Desktop\\ProgEnLab1\\list -w ')
        self.assertEqual(result, 0)
    #файл не найден
    def test_main(self):
        result = os.system('python3 lab1.py -t C:mshak_000\\Desktop\\ProgEnLab1\\text -r C:\\Users\\mshak_000\\Desktop\\ProgEnLab1\\list -w ')
        self.assertEqual(result, 2)
    #Аргумента не существует
    def test_main(self):
        result = os.system('python3 lab1.py -n C:mshak_000\\Desktop\\ProgEnLab1\\text -r C:\\Users\\mshak_000\\Desktop\\ProgEnLab1\\list -w ')
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
