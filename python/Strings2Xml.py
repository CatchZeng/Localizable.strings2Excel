# -*- coding:utf-8 -*-

import codecs
from optparse import OptionParser
from XmlFileUtil import XmlFileUtil
from StringsFileUtil import StringsFileUtil
from Log import Log
import time
import os


def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--fileDir",
                      help="strings files directory.",
                      metavar="filePath")

    parser.add_option("-t", "--targetDir",
                      help="The directory where the xml files will be saved.",
                      metavar="targetDir")

    parser.add_option("-a", "--additional",
                      help="additional info.",
                      metavar="additional")

    (options, args) = parser.parse_args()
    Log.info("options: %s, args: %s" % (options, args))

    return options


def startConvert(options):
    fileDir = options.fileDir

    if fileDir is None:
        Log.error("strings files directory can not be empty! try -h for help.")
        return

    if options.targetDir is None:
        Log.error("target files directory can not be empty! try -h for help.")
        return

    targetDir = options.targetDir + "/strings-files-to-xml_" + \
        time.strftime("%Y%m%d_%H%M%S")

    for _, _, filenames in os.walk(fileDir):
        stringsFilenames = [fi for fi in filenames if fi.endswith(".strings")]
        for filename in stringsFilenames:
            path = fileDir+"/"+filename
            (keys, values) = StringsFileUtil.getKeysAndValues(path)
            XmlFileUtil.writeToFile(keys, values, targetDir,
                                    filename.replace(".strings", ".xml"), options.additional)

    Log.info("Convert successfully! you can see xml files in %s" % (targetDir))


def main():
    options = addParser()
    startConvert(options)


main()
