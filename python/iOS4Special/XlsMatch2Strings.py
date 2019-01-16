# -*- coding:utf-8 -*-

import os
import sys
sys.path.append("../")
from optparse import OptionParser
from XlsFileUtil import XlsFileUtil

def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filePath",
                      help="original.xls File Path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFloderPath",
                      help="Target Floder Path.",
                      metavar="targetFloderPath")

    (options, args) = parser.parse_args()

    return options

# 根据xls中的内容，匹配strings中的key，替换掉value
def startConvert(options):
    folderPath = options.filePath
    targetFloderPath = options.targetFloderPath

    if not os.path.exists(targetFloderPath):
        os.makedirs(targetFloderPath)

    for parent, dirnames, filenames in os.walk(folderPath):
        xlsFilenames = [fi for fi in filenames if fi.endswith(".xls")]
        for xlsfile in xlsFilenames:
            xlsFileUtil = XlsFileUtil(folderPath+"/"+xlsfile)
            langFolderPath = targetFloderPath + "/" + xlsfile.replace(".xls", "")
            for sheet in xlsFileUtil.getAllTables():
                print "Sheet %s from %s" % (sheet.name, xlsfile)
                keyRow = sheet.row_values(0)
                for i in range(1, len(keyRow)):
                    # 根据语言分开替换
                    tmpname = keyRow[i]+".lproj/"+sheet.name
                    filename = targetFloderPath+"/"+tmpname
                    # print filename
                    if not os.path.exists(filename):
                        print "not exists %s" % filename
                        break
                    # print "start replace %s" % sheet.name
                    # 用文本打开文件，替换值，保存
                    file = open(filename, "r")
                    lines = file.readlines()
                    index = 0
                    count = len(lines)
                    # print count
                    rows = sheet.get_rows() # 重新读取，从头遍历
                    for row in rows:
                        key = "\"" + row[0].value + "\""
                        if "keyName" in key:
                            continue # 第一行忽略

                        # print row[i].value
                        content = "%s = \"%s\";\n" % (key, row[i].value) # key + " = " + "\"" + row[i].value + "\";\n"
                        # print content
                        
                        for j in range(index, count):
                            index += 1
                            line = lines[j]
                            # print "%s - %s" % (key, index) 
                            # 匹配key并替换行
                            if key in line:
                                lines[j] = content
                                # print j
                                break
                    file = open(filename, "w")
                    file.writelines(lines)
                    file.close()
                    print "File translated to %s" % tmpname
                    # break
            # break


def main():
    options = addParser()
    startConvert(options)
    

main()