# -*- coding:utf-8 -*-

from optparse import OptionParser
from XlsFileUtil import XlsFileUtil
from XmlFileUtil import XmlFileUtil
from StringsFileUtil import StringsFileUtil
from Log import Log
import os
import time


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--fileDir",
                      help="Xls files directory.",
                      metavar="fileDir")

    parser.add_option("-t", "--targetDir",
                      help="The directory where the xml files will be saved.",
                      metavar="targetDir")

    parser.add_option("-e", "--excelStorageForm",
                      type="string",
                      default="multiple",
                      help="The excel(.xls) file storage forms including single(single file), multiple(multiple files), default is multiple.",
                      metavar="excelStorageForm")

    parser.add_option("-a", "--additional",
                      help="additional info.",
                      metavar="additional")

    (options, args) = parser.parse_args()
    Log.info("options: %s, args: %s" % (options, args))

    return options


def convertFromSingleForm(options, fileDir, targetDir):
    for _, _, filenames in os.walk(fileDir):
        xlsFilenames = [fi for fi in filenames if fi.endswith(".xls")]
        for file in xlsFilenames:
            xlsFileUtil = XlsFileUtil(fileDir+"/"+file)
            table = xlsFileUtil.getTableByIndex(0)
            firstRow = table.row_values(0)
            keys = table.col_values(0)
            del keys[0]

            for index in range(len(firstRow)):
                if index <= 0:
                    continue
                languageName = firstRow[index]
                values = table.col_values(index)
                del values[0]

                if languageName == "zh-Hans":
                    languageName = "zh-rCN"

                path = targetDir + "/values-"+languageName+"/"
                if languageName == 'en':
                    path = targetDir + "/values/"
                filename = file.replace(".xls", ".xml")
                XmlFileUtil.writeToFile(
                    keys, values, path, filename, options.additional)
    print "Convert %s successfully! you can xml files in %s" % (
        fileDir, targetDir)


def convertFromMultipleForm(options, fileDir, targetDir):
    for _, _, filenames in os.walk(fileDir):
        xlsFilenames = [fi for fi in filenames if fi.endswith(".xls")]
        for file in xlsFilenames:
            xlsFileUtil = XlsFileUtil(fileDir+"/"+file)

            languageName = file.replace(".xls", "")
            if languageName == "zh-Hans":
                languageName = "zh-rCN"
            path = targetDir + "/values-"+languageName+"/"
            if languageName == 'en':
                path = targetDir + "/values/"
            if not os.path.exists(path):
                os.makedirs(path)

            for table in xlsFileUtil.getAllTables():
                keys = table.col_values(0)
                values = table.col_values(1)
                filename = table.name.replace(".strings", ".xml")

                XmlFileUtil.writeToFile(
                    keys, values, path, filename, options.additional)
    print "Convert %s successfully! you can xml files in %s" % (
        fileDir, targetDir)


def startConvert(options):
    fileDir = options.fileDir
    targetDir = options.targetDir

    print "Start converting"

    if fileDir is None:
        print "xls files directory can not be empty! try -h for help."
        return

    if targetDir is None:
        print "Target file path can not be empty! try -h for help."
        return

    targetDir = targetDir + "/xls-files-to-xml_" + \
        time.strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    if options.excelStorageForm == "single":
        convertFromSingleForm(options, fileDir, targetDir)
    else:
        convertFromMultipleForm(options, fileDir, targetDir)


def main():
    options = addParser()
    startConvert(options)


main()
