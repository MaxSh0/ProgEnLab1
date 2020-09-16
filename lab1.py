import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', action="store", dest="PathText")
parser.add_argument('-w', action="store", dest="Symbol")
parser.add_argument('-l', action="store", dest="PathList", default=None)
args = parser.parse_args()
print(args)

text = open(args.PathText)
text = text.read()

List = open(args.PathList)
List = List.read()

text = text.replace(List,args.Symbol)

print(text)









