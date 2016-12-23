# -*- coding:utf-8 -*-

import codecs
import pyExcelerator
import sys
import os
from optparse import OptionParser

#Add command option
def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filePath",
                      help="Localizable.strings file path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFilePath",
                      help="strings.xml file Path.",
                      metavar="targetFilePath")

    parser.add_option("-a", "--additionalInfo",
                      help="Additional info.",
                      metavar="additionalInfo")

    (options, args) = parser.parse_args()

    return options


# Start convert Localizable.strings to android strings.xml
def startConvert(options):
    filePath = options.filePath
    targetFilePath = options.targetFilePath
    additionalInfo = options.additionalInfo

    if filePath is not None:
        # ------------------------------ iOS ---------------------------
        print "Read Localizable.strings file from %s" % (filePath)

        # 1.Read localizable.strings
        file = codecs.open(filePath, 'r', 'utf-8')
        string = file.read()
        file.close()

        # 2.Split by ";
        localStringList = string.split('\";')
        list = [x.split(' = ') for x in localStringList]

        print "Read Localizable.strings finish"

        if targetFilePath is not None:
            filePath = targetFilePath
            if (not targetFilePath.endswith(".xml")):
                filePath = targetFilePath + "/strings.xml"

            # ------------------------------ Android ---------------------------
            print "Writing data to target file"

            # 1.open file
            fo = open(filePath, "wb")

            # 2.write header data
            xmlHeader = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
            fo.write(xmlHeader)

            # Add two columns data
            for x in range(len(list)):
                keyValue = list[x];
                if len(keyValue) > 1:
                    string0 = keyValue[0]
                    string1 = keyValue[1]
                    string0 = string0.split('\"')[1]
                    string1 = string1[1:]
                    stringcontent = "   <string name=\"" + string0 + "\">" + string1 + "</string>\n"
                    fo.write(stringcontent.encode('utf-8'));

            # Save to target file path
            if additionalInfo is not None:
                fo.write(additionalInfo)

            fo.write("</resources>");

            # Close file
            fo.close()

            print "Convert successfully! you can see strings.xml in %s" % (filePath)

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


