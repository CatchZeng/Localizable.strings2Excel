# -*- coding:utf-8 -*-

import pyExcelerator
import sys
from optparse import OptionParser

#Add command option
def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filePath",
                      help="Localizable.xls file path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFilePath",
                      help="Localizable.strings file path.",
                      metavar="targetFilePath")

    (options, args) = parser.parse_args()

    return options

# Start convert Localizable.xls to Localizable.strings
def startConvert(options):
    filePath = options.filePath
    targetFilePath = options.targetFilePath

    if filePath is not None:
        if (not filePath.endswith(".xls")):
            print "File path %s is not correct,Please check it!" % (filePath)
            return

        print "Read Localizable.xls file from %s" % (filePath)

        # Get all sheets
        sheets = pyExcelerator.parse_xls(filePath)
        # Get first sheet all data
        sheet = sheets[0]
        tuple = sheet[1]

        length = len(tuple) / 2

        # Record first column data
        list0 = []
        for x in range(length):
            if tuple[x, 0]:
                string = tuple[x, 0]
                list0.append(string)

        print("First column:\n")
        print(list0)

        # Record second column data
        list1 = []
        for x in range(length):
            if tuple[x, 1]:
                string = tuple[x, 1]
                list1.append(string)

        print("Second column:\n")
        print(list1)

        if targetFilePath is not None:
            print "Writing data to target file"

            # Output to Localizable.strings
            wirtePath = targetFilePath
            if (not targetFilePath.endswith(".strings")):
                wirtePath = targetFilePath + "/LocalizableBack.strings"

            fo = open(wirtePath, "wb")

            for x in range(len(list0)):
                if list0[x] and list1[x]:
                    string0 = list0[x]
                    string1 = list1[x]
                    stringcontent = "\"" + string0 + "\" " + "= " + "\"" + string1 + "\";\n"
                    fo.write(stringcontent);

            # Close file
            fo.close()
            print "Convert successfully! you can see strings file in %s" % (wirtePath)

        else:
            print "Target file path can not be empty! try -h for help."

    else:
        print "File path can not be empty! try -h for help."

    return

# Mian
def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    options = addParser()
    startConvert(options)

    return


#Start
main()