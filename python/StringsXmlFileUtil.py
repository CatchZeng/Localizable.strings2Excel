#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from Log import Log

class StringsXmlFileUtil:
    'android strings.xml file util'

    @staticmethod
    def writeToFile(keys, values,directory,additional):
        if not os.path.exists(directory):
            os.makedirs(directory)

        Log.info("Creating android file:" + directory + "/strings.xml")

        fo = open(directory + "/strings.xml", "wb")

        stringEncoding = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
        fo.write(stringEncoding)

        for x in range(len(keys)):
            if values[x] is None or values[x] == '' :
                Log.error("Key:" + keys[x] + "\'s value is None. Index:" + str(x + 1))
                continue

            key = keys[x]
            value = values[x]
            content = "   <string name=\"" + key + "\">" + value + "</string>\n"
            fo.write(content);

        if additional is not None:
            fo.write(additional)

        fo.write("</resources>");
        fo.close()