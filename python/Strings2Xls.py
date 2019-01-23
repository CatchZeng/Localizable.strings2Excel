# -*- coding:utf-8 -*-

import os
from optparse import OptionParser
from LocalizableStringsFileUtil import LocalizableStringsFileUtil
import pyExcelerator
import time

# Add command option


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--stringsDir",
                      help=".strings files directory.",
                      metavar="stringsDir")

    parser.add_option("-t", "--targetDir",
                      help="The directory where the excel(.xls) file will be saved.",
                      metavar="targetDir")

    (options, _) = parser.parse_args()

    return options


# Start convert .strings files to xls
def startConvert(options):
    stringsDir = options.stringsDir
    targetDir = options.targetDir

    print "Start converting"

    if stringsDir is None:
        print ".strings files directory can not be empty! try -h for help."
        return

    if targetDir is None:
        print "Target file directory can not be empty! try -h for help."
        return

    destDir = targetDir + "/strings-files-to-xls_" + \
        time.strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(destDir):
        os.makedirs(destDir)

    for _, dirnames, _ in os.walk(stringsDir):
        lprojDirs = [di for di in dirnames if di.endswith(".lproj")]
        for dirname in lprojDirs:
            workbook = pyExcelerator.Workbook()
            for _, _, filenames in os.walk(stringsDir+'/'+dirname):
                stringsFiles = [
                    fi for fi in filenames if fi.endswith(".strings")]
                for stringfile in stringsFiles:
                    ws = workbook.add_sheet(stringfile)

                    # Key & Value
                    path = stringsDir+dirname+'/' + stringfile
                    (keys, values) = LocalizableStringsFileUtil.getKeysAndValues(
                        path)
                    for keyIndex in range(len(keys)):
                        key = keys[keyIndex]
                        value = values[keyIndex]
                        ws.write(keyIndex, 0, key)
                        ws.write(keyIndex, 1, value)

            filePath = destDir + "/" + dirname.replace(".lproj", "") + ".xls"
            workbook.save(filePath)

    print "Convert %s successfully! you can see xls file in %s" % (
        stringsDir, filePath)


def main():
    options = addParser()
    startConvert(options)


main()
