# -*- coding:utf-8 -*-

import os
from optparse import OptionParser
from LocalizableStringsFileUtil import LocalizableStringsFileUtil
import pyExcelerator
import time

# Add command option


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filesDirectory",
                      help="Localizable.strings files directory.",
                      metavar="filesDirectory")

    parser.add_option("-t", "--targetFilePath",
                      help="Target File (xls) Path.",
                      metavar="targetFilePath")

    (options, args) = parser.parse_args()

    return options


# Start convert Localizable.strings to xls
def startConvert(options):
    directory = options.filesDirectory
    targetFilePath = options.targetFilePath

    if directory is not None:
        index = 0
        if targetFilePath is not None:
            workbook = pyExcelerator.Workbook()
            ws = workbook.add_sheet('Localizable.strings')

            for parent, dirnames, filenames in os.walk(directory):
                for dirname in dirnames:
                    # KeyName & CountryCode
                    if index == 0:
                        ws.write(0, 0, 'keyName')
                    conturyCode = dirname.split('.')[0]
                    ws.write(0, index+1, conturyCode)

                    # Key & Value
                    path = directory+'/'+dirname+'/Localizable.strings'
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

            filePath = targetFilePath + "/Localizable.xls"
            workbook.save(filePath)
            print "Convert successfully! you can see xls file in %s" % (
                filePath)

        else:
            print "Target file path can not be empty! try -h for help."
    else:
        print "Localizable.strings files directory can not be empty! try -h for help."


def main():
    options = addParser()
    startConvert(options)


main()
