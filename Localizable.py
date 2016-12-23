# -*- coding:utf-8 -*-

import codecs
import pyExcelerator
from optparse import OptionParser

#Add command option
def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filePath",
                      help="Localizable.strings file path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFilePath",
                      help="Target(Localizable.xls) file path.",
                      metavar="targetFilePath")

    (options, args) = parser.parse_args()

    return options


# Start convert localizable.strings to localizable.xls
def startConvert(options):
    filePath = options.filePath
    targetFilePath = options.targetFilePath

    if filePath is not None:
        if (not filePath.endswith(".strings")):
            print "File path %s is not correct,Please check it!" % (filePath)
            return

        print "Read Localizable.strings from %s" % (filePath)

        # 1.Read localizable.strings
        file = codecs.open(filePath, 'r', 'utf-8')
        string = file.read()
        file.close()

        # 2.Split by ";
        localStringList = string.split('\";')
        list = [x.split(' = ') for x in localStringList]

        print "Read Localizable.strings finish"

        if targetFilePath is not None:
            print "Writing data to target file"

            workbook = pyExcelerator.Workbook()
            ws = workbook.add_sheet('Localizable.strings')

            # Add two columns data
            for x in range(len(list)):
                for y in range(len(list[x])):
                    if list[x][y]:
                        keyOrValue = list[x][y]
                        if y == 0:
                            keyString = keyOrValue.split('\"')
                            if(len(keyString) > 1):
                                ws.write(x, y, keyString[1])
                            else:
                                print "This is an empty line"
                        else:
                            value = keyOrValue[1:]
                            ws.write(x, y, value)

            #Save to target file path
            filePath = targetFilePath
            if (not targetFilePath.endswith(".xls")):
                filePath = targetFilePath + "/Localizable.xls"

            workbook.save(filePath)

            print "Convert successfully! you can see xls in %s" % (filePath)

        else:
            print "Target file path can not be empty! try -h for help."

    else:
        print "File path can not be empty! try -h for help."

    return


# Mian
def main():
    options = addParser()
    startConvert(options)

    return

#Start
main()

