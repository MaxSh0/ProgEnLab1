import argparse

#Функция замены слова на определение в словаре
def Vocabulary(text,list):
    words = list.split('\n')
    vocabulary =[]
    for word in words:
        word = word.split()
        vocabulary.append(word)

    for definition in vocabulary:
        text = text.replace(definition[0], definition[1])
    return text

#Функция замены слов на символы
def Сensorship(text,list):
    words = list.split()
    for word in words:
        text = text.replace(word,args.Symbol*len(word))
    return text

#Создаем экземпляр класса argparser
parser = argparse.ArgumentParser()

#Добавляем агрументы командной строки
parser.add_argument('-t','--text', action="store", dest='PathText', help='Путь к текстовому файлу')
parser.add_argument('-r','--relpace', action="store", dest='PathList', help='Путь к черному списку/словарю')
parser.add_argument('-w','--with', action="store", dest='Symbol', help='Символ для замены')
parser.add_argument('-d','--dict', action="store_true", dest='Dict', help='Признак использования словаря')
parser.add_argument('-v','--timeit',action="store_true", help='Если установлен выводится время работы программы')

#Считываем переданные аргументы
args = parser.parse_args()
print(args)

#Открываем файл с исходным текстом
text = open(args.PathText).read()
# Открываем список слов
list = open(args.PathList).read()

# Если флаг установлен заменяем слова на слова из словаря, иначе на символ
if args.Dict:
    text = Vocabulary(text,list)
else:
    text = Сensorship(text,list)

print(text)

if(args.timeit):
    print("time:")
# время выполнения TODO




