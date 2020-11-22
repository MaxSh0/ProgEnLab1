import argparse
import re
import sys
import time


# Наследник класса парсера с измененными методами ошибки и предупреждения
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

    def warning(self,message):
        sys.stderr.write('WARNING: %s\n' % message)

#Проверка строки пути на корректность
def ErrorPath(Part):
    if (isinstance(Part, str) == False):
        return 0
    elif (re.match(r'\w:(\\{0,2}\w+)+', Part) != None):
        return 1
    else:
        return 0

#Проверка замещающего символа на корректность
def ErrorSymbol(Symbol):
    if(len(Symbol) == 1):
        return 1
    else:
        return 0

#Функция замены слова на определение в словаре
def Vocabulary(text,list):
    words = list.split('\n')# O(M)
    vocabulary =[]
    for word in words:# O(M)
        word = word.split() # O(1)
        if(len(word)>0): # O(1)
            vocabulary.append(word)# O(1)
    for definition in vocabulary: # O(M)
        text = text.replace(definition[0], definition[1])# O(N*M)               O(M + M + M*(N*M)) = O(M*2 + M^2 * NM)
    return text

#Функция замены слов на символы
def Сensorship(text,list,symbol):
    words = list.split() # O(M)
    for word in words: # O(M)
        text = text.replace(word,symbol*len(word)) # O(N*M)      O(M + M * (N*M)) = O(M + MN * M^2)
    return text
if __name__ == '__main__':
    #Создаем экземпляр класса argparser
    parser = MyParser()

    #Добавляем агрументы командной строки
    parser.add_argument('-t','--text', action="store", dest='PathText', help='Путь к текстовому файлу')
    parser.add_argument('-r','--relpace', action="store", dest='PathList', help='Путь к черному списку/словарю')
    parser.add_argument('-w','--with', action="store", dest='Symbol', help='Символ для замены (1 символ)')
    parser.add_argument('-d','--dict', action="store_true", dest='Dict', help='Признак использования словаря')
    parser.add_argument('-v','--timeit',action="store_true", help='Если установлен выводится время работы программы')

    #Считываем переданные аргументы
    args = parser.parse_args()

    if (re.search(r'\.txt', args.PathText) == None):
        args.PathText = args.PathText + ".txt"
    if (re.search(r'\.txt', args.PathList) == None):
        args.PathList = args.PathList + ".txt"

    #Проверяем корректность введенного символа
    if(args.Symbol != None):
        if(ErrorSymbol(args.Symbol) == 0):
            parser.error("Символ не удовлетворяет условиям")

    #Предупреждаем о избыточном синтаксисе
    if(args.Symbol != None):
        if(ErrorSymbol(args.Symbol) == 1 and args.Dict == True):
            parser.warning("Установлен флаг словаря и введен символ")

    #Обрабатываем ошибку пути
    if(ErrorPath(args.PathText) == 0):
        parser.error("Неверно указан путь к текстовому файлу")

    #Открываем файл с исходным текстом
    try:
        text = open(args.PathText).read()
    except OSError as e:
        parser.error("Текстовый файл не найден")
    # Обрабатываем ошибку пути
    if(ErrorPath(args.PathList) == 0):
        parser.error("Неверно указан путь к словарю")
    try:
        # Открываем список слов
        list = open(args.PathList).read()
    except OSError as e:
        parser.error("Текстовый файл словаря не найден")

    #Начинаем отсчет времени
    start_time = time.time()
    # Если флаг установлен заменяем слова на слова из словаря, иначе на символ
    if args.Dict:
        start_time = time.time()
        text = Vocabulary(text,list)
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        start_time = time.time()
        text = Сensorship(text,list,args.Symbol)
        print("--- %s seconds ---" % (time.time() - start_time))




