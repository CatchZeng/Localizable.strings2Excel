# -*- coding:utf-8 -*-

import codecs
import pyExcelerator

file = codecs.open('en.js', 'r', 'utf-8')
string = file.read()
print (string)
file.close()

# 使用\n分割数据
list = string.split('\n');

# 记录空行数据 和 注释 的下标
listIndex = []
for x in range(len(list)):
    stringTmp = list[x]
    if len(stringTmp) < 1 or stringTmp.startswith("//"):
        listIndex.append(x)
print(listIndex)

# 删除空行数据
startIndex = listIndex[0]
deleteIndexCount = 0
for index in listIndex:
    if index == startIndex:
        del list[index]
    else:
        deleteIndexCount += 1
        del list[index - deleteIndexCount]

# 删除前面四个数据 u'// This file was automatically generated.  Do not modify.' u'\\'use strict\\';' u'goog.provide(\\'Blockly.Msg.en\\');' u'goog.require(\\'Blockly.Msg\\');'
del list[0]
del list[0]
del list[0]
print(list)

workbook = pyExcelerator.Workbook()
ws = workbook.add_sheet('en.js')

# 使用=分割数据,并写入数据
for index in range(len(list)):
    stringRow = list[index]
    stringKey = stringRow.split('=')[0]
    print (stringKey)
    ws.write(index, 0, stringKey)

workbook.save('JSLocalizable.xls')
