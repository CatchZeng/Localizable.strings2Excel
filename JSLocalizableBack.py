# -*- coding:utf-8 -*-

import pyExcelerator
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 获取所有sheets
sheets = pyExcelerator.parse_xls('JSLocalizableBack.xls')
# 获取第一个sheet的所有数据
sheet = sheets[0]
tuple = sheet[1]

length = len(tuple) / 2

# 记录第0列数据
list0 = []
for x in range(length):
    if tuple[x, 0]:
        string = tuple[x, 0]
        list0.append(string)

print("第0列数据:\n")
print(list0)

# 记录第1列数据
list1 = []
for x in range(length):
    if tuple[x, 1]:
        string = tuple[x, 1]
        list1.append(string)

print("第1列数据:\n")
print(list1)

# 输出到Localizable.strings

# 打开一个文件
fo = open("JSLocalizableBack.js", "wb")

stringAdd = "// This file was automatically generated.  Do not modify.\n\n'use strict';\n\ngoog.provide('Blockly.Msg.en');\n\ngoog.require('Blockly.Msg');\n\n"
fo.write(stringAdd);

for x in range(len(list0)):
    if list0[x] and list1[x]:
        string0 = list0[x]
        string1 = list1[x]
        stringcontent = string0 + " = " + "\"" + string1 + "\";\n"
        fo.write(stringcontent);

# 关闭打开的文件
fo.close()
