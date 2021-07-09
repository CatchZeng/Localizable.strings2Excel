# Adapted from Transifex: https://github.com/transifex/transifex/blob/master/transifex/resources/formats/strings.py
# -*- coding: utf-8 -*-
# GPLv2

"""
Apple strings file handler/compiler
"""

from __future__ import absolute_import
import codecs, re, chardet


"""
Handler for Apple STRINGS translation files.

Apple strings files *must* be encoded in cls.ENCODING encoding.
"""

format_encoding = 'UTF-16'

def _unescape_key(s):
    return s.replace('\\\n', '')

def _unescape(s):
    s = s.replace('\\\n', '')
    return s.replace('\\"', '"').replace(r'\n', '\n').replace(r'\r', '\r')

def _get_content(filename=None, content=None):
    if content is not None:
        if chardet.detect(content)['encoding'].startswith(format_encoding):
            encoding = format_encoding
        else:
            encoding = 'UTF-8'
        if isinstance(content, str):
            content.decode(encoding)
        else:
            return content
    if filename is None:
        return None
    return _get_content_from_file(filename, format_encoding)

def _get_content_from_file(filename, encoding):
    f = open(filename, 'rb')
    try:
        content = f.read()
        if chardet.detect(content)['encoding'].startswith(format_encoding):
            #f = f.decode(format_encoding)
            encoding = format_encoding
        else:
            #f = f.decode(default_encoding)
            encoding = 'utf-8'
        f.close()
        f = codecs.open(filename, 'r', encoding=encoding)
        return f.read()
    except IOError as e:
        print("Error opening file %s with encoding %s: %s" %\
                (filename, format_encoding, e.message))
    except Exception as e:
        print("Unhandled exception: %s" % e.message)
    finally:
        f.close()

def parse_strings(content="", filename=None):
    """Parse an apple .strings file and create a stringset with
    all entries in the file.

    See
    http://developer.apple.com/library/mac/#documentation/MacOSX/Conceptual/BPInternational/Articles/StringsFiles.html
    for details.
    """
    if filename is not None:
        content = _get_content(filename=filename)

    stringset = []
    f = content
    if f.startswith(u'\ufeff'):
        f = f.lstrip(u'\ufeff')
    #regex for finding all comments in a file
    cp = r'(?:/\*(?P<comment>(?:[^*]|(?:\*+[^*/]))*\**)\*/)'
    p = re.compile(r'(?:%s[ \t]*[\n]|[\r\n]|[\r]){0,1}(?P<line>(("(?P<key>[^"\\]*(?:\\.[^"\\]*)*)")|(?P<property>\w+))\s*=\s*"(?P<value>[^"\\]*(?:\\.[^"\\]*)*)"\s*;)'%cp, re.DOTALL|re.U)
    #c = re.compile(r'\s*/\*(.|\s)*?\*/\s*', re.U)
    c = re.compile(r'//[^\n]*\n|/\*(?:.|[\r\n])*?\*/', re.U)
    ws = re.compile(r'\s+', re.U)
    end=0
    start = 0
    for i in p.finditer(f):
        start = i.start('line')
        end_ = i.end()
        key = i.group('key')
        comment = i.group('comment') or ''
        if not key:
            key = i.group('property')
        value = i.group('value')
        while end < start:
            m = c.match(f, end, start) or ws.match(f, end, start)
            if not m or m.start() != end:
                print("Invalid syntax: %s" %\
                        f[end:start])
            end = m.end()
        end = end_
        key = _unescape_key(key)
        stringset.append({'key': key, 'value': _unescape(value), 'comment': comment})
    return stringset
