# -*- coding:utf-8 -*-

import codecs
import pyExcelerator
from optparse import OptionParser

#Add Command Option
def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filePath",
                      help="File (Localizable.strings) Path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFilePath",
                      help="Target File (Localizable.xls) Path.",
                      metavar="targetFilePath")

    (options, args) = parser.parse_args()
    # print "options: %s, args: %s" % (options, args)

    return options


# Start Convert Localizable.strings To  Localizable.xls
def startConvert(options):
    filePath = options.filePath
    targetFilePath = options.targetFilePath

    if filePath is not None:
        if (not filePath.endswith(".strings")):
            print "File path %s is not correct,Please check it!" % (filePath)
            return

        print "Read Localizable.strings from %s" % (filePath)

        # 1.Read Localizable.strings
        file = codecs.open(filePath, 'r', 'utf-8')
        string = file.read()
        file.close()

        # 2.Split By ";
        localStringList = string.split('\";')
        list = [x.split(' = ') for x in localStringList]

        print "Read Finish"

        if targetFilePath is not None:
            print "Writing data to target file"

            workbook = pyExcelerator.Workbook()
            ws = workbook.add_sheet('Localizable.strings')

            # Add Two Columns Data
            for x in range(len(list)):
                for y in range(len(list[x])):
                    if list[x][y]:
                        string3 = list[x][y]
                        if y == 0:
                            list3 = string3.split('\"')
                            if(len(list3) > 1):
                                ws.write(x, y, list3[1])
                            else:
                                print "This is an empty line"
                        else:
                            value = string3[1:]
                            ws.write(x, y, value)

            #Save To Target File Path
            filePath = targetFilePath
            if (not targetFilePath.endswith(".xls")):
                filePath = targetFilePath + "/Localizable.xls"

            workbook.save(filePath)

            print "Success! you can see xls in %s" % (filePath)

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

