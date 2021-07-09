import codecs, re

class StringsFile:
    'iOS Localizable.strings file'

    def __init__(self, path=None) -> None:
        self.path = path

    def parse(self):
        if self.path is None:
            return
        content = self._get_content()
        if content is None:
            return

        stringset = []
        f = content
        f = _remove_BOM(f)
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

    def _get_content(self):
        encodings = ['utf-8', 'utf-16']
        for e in encodings:
            try:
                file = codecs.open(self.path, 'r', encoding=e)
                content = file.read()
                file.close()
                return content
            except Exception as e:
                print("get content exception: %s" % e.message)
            finally:
                file.close()

def _unescape_key(s):
    return s.replace('\\\n', '')

def _unescape(s):
    s = s.replace('\\\n', '')
    return s.replace('\\"', '"').replace(r'\n', '\n').replace(r'\r', '\r')

def _remove_BOM(s):
    if s.startswith(u'\ufeff'):
        return s.lstrip(u'\ufeff')
    return s