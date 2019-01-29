#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from Log import Log
import xml.dom.minidom
import re


class XmlFileUtil:
    'android strings.xml file util'

    @staticmethod
    def writeToFile(keys, values, directory, filename, additional):
        if not os.path.exists(directory):
            os.makedirs(directory)

        fo = open(directory + "/" + filename, "wb")

        stringEncoding = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
        fo.write(stringEncoding)

        for x in range(len(keys)):
            if values[x] is None or values[x] == '':
                Log.error("Key:" + keys[x] +
                          "\'s value is None. Index:" + str(x + 1))
                continue

            key = keys[x].strip()
            value = re.sub(r'(%\d\$)(@)', r'\1s', values[x])
            content = "   <string name=\"" + key + "\">" + value + "</string>\n"
            fo.write(content)

        if additional is not None:
            fo.write(additional)

        fo.write("</resources>")
        fo.close()

    @staticmethod
    def getKeysAndValues(path):
        if path is None:
            Log.error('file path is None')
            return

        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        itemlist = root.getElementsByTagName('string')

        keys = []
        values = []
        for index in range(len(itemlist)):
            item = itemlist[index]
            key = item.getAttribute("name")
            value = item.firstChild.data
            keys.append(key)
            values.append(value)

        return (keys, values)
