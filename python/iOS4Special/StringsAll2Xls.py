# -*- coding:utf-8 -*-

import os
import sys
sys.path.append("../")
from optparse import OptionParser
from LocalizableStringsFileUtil import LocalizableStringsFileUtil
import pyExcelerator

#Add command option
def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filesDirectory",
                      help="Project files (strings) directory.",
                      metavar="filesDirectory")

    parser.add_option("-t", "--targetDirectory",
                      help="Target files (xls) directory.",
                      metavar="targetDirectory")

    (options, args) = parser.parse_args()

    return options


# Start convert all *.strings to xls
def startConvert(options):
    directory = options.filesDirectory
    targetDirectory = options.targetDirectory

    if directory is not None:
        if targetDirectory is not None:
            # 找到一个lproj，把其中的strings都列出来，分别导出表
            for parent, dirnames, _ in os.walk(directory):
                for dirname in dirnames:
                    if ".lproj" not in dirname:
                        continue
                    if "Base.lproj" in dirname:
                        continue
                    # print dirname
                    for _, _, filenames in os.walk(directory+'/'+dirname):
                        for filename in filenames:
                            print filename
                            export(options, filename)
                    break

            # export(options)

        else:
            print "Target directory path can not be empty! try -h for help."
    else:
        print "Project files directory can not be empty! try -h for help."

def export(options, filename):
    directory = options.filesDirectory
    targetDirectory = options.targetDirectory
    index = 0

    workbook = pyExcelerator.Workbook()
    ws = workbook.add_sheet(filename) # ('*.strings')

    for parent, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            # 排除非多语言资源目录
            if ".lproj" not in dirname:
                continue
            if "Base.lproj" in dirname:
                continue

            # KeyName & CountryCode
            if index == 0:
                ws.write(0,0,'keyName')
            conturyCode = dirname.split('.')[0]
            ws.write(0,index+1,conturyCode)

            # Key & Value
            path = directory+'/'+dirname+'/'+filename # '/*.strings'
            (keys, values) = LocalizableStringsFileUtil.getKeysAndValues(path)
            for x in range(len(keys)):
                key = keys[x]
                value = values[x]
                if (index == 0):
                    ws.write(x+1, 0, key)
                    ws.write(x+1, 1, value)
                else:
                    ws.write(x+1, index + 1, value)
            index += 1

    xlsName = filename.replace(".strings", ".xls")
    filePath = targetDirectory+'/'+xlsName # "/*.xls"
    workbook.save(filePath)
    print "Convert xls file in %s" % (filePath)

def main():
    options = addParser()
    startConvert(options)

main()
