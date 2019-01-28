# -*- coding:utf-8 -*-

from optparse import OptionParser
from XlsFileUtil import XlsFileUtil
from StringsXmlFileUtil import StringsXmlFileUtil
from StringsFileUtil import StringsFileUtil
from Log import Log
import os


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filePath",
                      help="original.xls File Path.",
                      metavar="filePath")

    parser.add_option("-t", "--targetFloderPath",
                      help="Target Floder Path.",
                      metavar="targetFloderPath")

    parser.add_option("-i", "--iOSAdditional",
                      help="iOS additional info.",
                      metavar="iOSAdditional")

    parser.add_option("-a", "--androidAdditional",
                      help="android additional info.",
                      metavar="androidAdditional")

    (options, args) = parser.parse_args()
    Log.info("options: %s, args: %s" % (options, args))

    return options


def startConvert(options):
    filePath = options.filePath
    targetFloderPath = options.targetFloderPath
    iOSAdditional = options.iOSAdditional
    androidAdditional = options.androidAdditional

    if filePath is not None:
        if targetFloderPath is None:
            Log.error("targetFloderPath is None！use -h for help.")
            return

        # xls
        Log.info("read xls file from"+filePath)
        xlsFileUtil = XlsFileUtil(filePath)

        # iOS & Android
        table = xlsFileUtil.getTableByIndex(0)
        convertiOSAndAndroidFile(
            table, targetFloderPath, iOSAdditional, androidAdditional)

        Log.info("Finished,go to see it -> "+targetFloderPath)

    else:
        Log.error("file path is None！use -h for help.")


def convertiOSAndAndroidFile(table, targetFloderPath, iOSAdditional, androidAdditional):
    firstRow = table.row_values(0)

    keys = table.col_values(0)
    del keys[0]

    for index in range(len(firstRow)):
        if index > 0:
            languageName = firstRow[index]
            values = table.col_values(index)
            del values[0]
            # iOS
            StringsFileUtil.writeToFile(
                keys, values, targetFloderPath + "/ios/"+languageName+".lproj/", "Localizable.strings", iOSAdditional)

            # Android
            if languageName == "zh-Hans":
                languageName = "zh-rCN"

            path = targetFloderPath + "/android/values-"+languageName+"/"
            if languageName == 'en':
                path = targetFloderPath + "/android/values/"
            StringsXmlFileUtil.writeToFile(
                keys, values, path, "/strings.xml", androidAdditional)


def main():
    options = addParser()
    startConvert(options)


main()
