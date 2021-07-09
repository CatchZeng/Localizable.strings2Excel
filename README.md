# Localizable.strings2Excel

Python command line tool for conversion between iOS strings files and excel files & between android strings.xml files and excl files. & strings files to android strings.xml files.

[中文请点击](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/README-CN.md)

## Features

- [x] Support convert **iOS** strings files to **excel** files.
- [x] Support convert **excel** files to **iOS** strings files.
- [x] Support convert **android** xml files to **excel** files.
- [x] Support convert **excel** files to **android** xml files.
- [x] Support convert **iOS** strings files to **android** xml files.

## Version

**V1.0.0**

## Required

### 1.Check python version

python version must be 2.x.

```
$ python --version
Python 2.7.10
```

### 2.Check pip(python package manager)

```
$ pip --version
pip 19.0 from /Library/Python/2.7/site-packages/pip (python 2.7)
```

if pip is not installed

```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
sudo python get-pip.py
```

### 3.Install pyexcelerator

```
sudo pip install pyExcelerator
```

### 4.Install xlrd

```
sudo pip install xlrd
```

## Usage

### 1.Convert **iOS** strings files to **excel** files.

```
$ python python/Strings2Xls.py -f examples/ios/ -t examples/output
Start converting
Convert examples/ios/ successfully! you can see xls file in examples/output/strings-files-to-xls_20190129_165830
```

![](imgs/1.0.0/strings-2-xls.jpg)

### 2.Convert **excel** files to **iOS** strings files

```
$ python python/Xls2Strings.py -f examples/output/strings-files-to-xls_20190129_165830/ -t examples/ou
tput/

options: {'fileDir': 'examples/output/strings-files-to-xls_20190129_165830/', 'targetDir': 'examples/output/', 'excelStorageForm': 'multiple', 'additional': None
}, args: []

Start converting
Convert examples/output/strings-files-to-xls_20190129_165830/ successfully! you can see strings file in examples/output//xls-files-to-strings_20190129_171146
```

![](imgs/1.0.0/xls-2-strings.jpg)

### 3.Convert **android** xml files to **excel** files

```
$ python python/Xml2Xls.py -f examples/android/ -t examples/output

options: {'fileDir': 'examples/android/', 'targetDir': 'examples/output', 'excelStorageForm': 'multiple'}, args: []

Start converting
Convert examples/android/ successfully! you can see xls file in examples/output/xml-files-to-xls_20190129_172938
```

![](imgs/1.0.0/xml-2-xls.jpg)

### 4.Convert **excel** files to **android** xml files

```
$ python python/Xls2Xml.py -f examples/output/xml-files-to-xls_20190129_172938/ -t examples/output/

options: {'fileDir': 'examples/output/xml-files-to-xls_20190129_172938/', 'targetDir': 'examples/output/', 'excelStorageForm': 'multiple', 'additional': None}, args
: []

Start converting
Convert examples/output/xml-files-to-xls_20190129_172938/ successfully! you can xml files in examples/output//xls-files-to-xml_20190129_174207
```

![](imgs/1.0.0/xls-2-xml.jpg)

### 5.Convert **iOS** strings files to **android** xml files.

```shell
$ python python/Strings2Xml.py -f examples/ios/en.lproj/ -t examples/output/

options: {'fileDir': 'examples/ios/en.lproj/', 'targetDir': 'examples/output/', 'additional': None}, args: []


Creating android file:examples/output//strings-files-to-xml_20190129_164122/Localizable.xml


Creating android file:examples/output//strings-files-to-xml_20190129_164122/InfoPlist.xml


Convert successfully! you can see xml files in examples/output//strings-files-to-xml_20190129_164122

```

![](imgs/1.0.0/strings-2-xml.jpg)

## ChangeLog

[ChangeLog](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/CHANGELOG.md)

## Thanks

- [Buguibu](https://github.com/buguibu)
- [vgutierrezNologis](https://github.com/vgutierrezNologis)
- [linguinan](https://github.com/linguinan)
- [qiusuo8](https://github.com/qiusuo8)
- [light-bo](https://github.com/light-bo)
- [bryant1410](https://github.com/bryant1410)
