import codecs
import pyExcelerator

file = codecs.open('Localizable.strings', 'r', 'utf-8')
string = file.read()
file.close()

string = string.replace('/* No comment provided by engineer. */', '').replace('\n', '')

list = [x.split(' = ') for x in string.split(';')]

workbook = pyExcelerator.Workbook()
ws = workbook.add_sheet('sheet1')

for x in range(len(list)):
    for y in range(len(list[x])):
        if list[x][y]:
            string3 = list[x][y]
            list3 = string3.split('\"')
            ws.write(x,y,list3[1])



file2 = codecs.open('en.js', 'r', 'utf-8')
string2 = file2.read()
file2.close()

string2 = string2.replace('/* No comment provided by engineer. */', '').replace('\n', '')

list2 = [x.split(' = ') for x in string2.split(';')]

ws2 = workbook.add_sheet('sheet2')

for x in range(len(list2)):
    for y in range(len(list2[x])):
        if list2[x][y]:
            ws2.write(x,y,list2[x][y])


workbook.save('localizable.xls')