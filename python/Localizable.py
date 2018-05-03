# -*- coding:utf-8 -*-

import os
from optparse import OptionParser
from LocalizableStringsFileUtil import LocalizableStringsFileUtil
import pyExcelerator
import time

#Add command option
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
        if targetFilePath is not None:
            destinyDir = targetFilePath + "/strings-files-to-xls_"+ time.strftime("%Y%m%d_%H%M%S")
            if not os.path.exists(destinyDir):
                os.makedirs(destinyDir)
            for parent, dirnames, unusedfilenames in os.walk(directory):
                lprogDirs = [di for di in dirnames if di.endswith(".lproj")]
                for dirname in lprogDirs:
                    workbook = pyExcelerator.Workbook()
                    for parent, dirnames2, filenames in os.walk(directory+'/'+dirname):
                        stringFiles = [fi for fi in filenames if fi.endswith(".strings")]
                        for stringfile in stringFiles:
                            ws = workbook.add_sheet(stringfile)

                            # Key & Value
                            path = directory+dirname+'/' + stringfile
                            (keys, values) = LocalizableStringsFileUtil.getKeysAndValues(path)
                            for keyIndex in range(len(keys)):
                                key = keys[keyIndex]
                                value = values[keyIndex]
                                ws.write(keyIndex, 0, key)
                                ws.write(keyIndex, 1, value)
                    
                    filePath = destinyDir +"/" + dirname.replace(".lproj", "") + ".xls"
                    workbook.save(filePath)
            print "Convert %s successfully! you can see xls file in %s" % (directory ,filePath)
        else:
            print "Target file path can not be empty! try -h for help."
    else:
        print "Localizable.strings files directory can not be empty! try -h for help."


def main():
    options = addParser()
    startConvert(options)

main()
