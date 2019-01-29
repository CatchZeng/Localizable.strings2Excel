# Localizable.strings2Excel

Python command line tool for conversion between iOS Localizable.strings and excel file & Localizable.strings to android strings.xml file.

[中文请点击](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/README-CN.md)

## Features

#### Convert iOS Localizable.strings files to excel.

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)

#### Convert Android strings.xml files to excel.

![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/atox.jpg)

#### Convert excel file to iOS & Android Localizable files.

![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)

#### Convert iOS Localizable.strings file to Android strings.xml file.

![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg)

#### Extract strings to xls

![extract strings to xls](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/strings2xls.jpg)

#### Convert xls to strings

![convert xls to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/xls2strings.jpg)

## ChangeLog

[ChangeLog](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/CHANGELOG.md)

## Environment

### 1.Check pip(python package manager)

```
$ pip --version
pip 19.0 from /Library/Python/2.7/site-packages/pip (python 2.7)
```

if pip is not installed

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py
```

### 2.Install pyexcelerator

```
sudo pip install pyExcelerator
```

### 3.Install xlrd

```
sudo pip install xlrd
```

## Usage

#### Convert iOS Localizable.strings files to excel.

```shell
python Localizable.py -f xxx/xxx -t xxx/xxx.xls

$ python Localizable.py -h
Usage: Localizable.py [options]

Options:
  -h, --help            show this help message and exit
  -f filesDirectory, --filesDirectory=filesDirectory
                        Localizable.strings files directory.
  -t targetFilePath, --targetFilePath=targetFilePath
                        Target File (xls) Path.
```

#### Convert Android strings.xml files to excel.

```shell
python LocalizableStringsXml.py -f xxx/xxx -t xxx/xxx.xls

python LocalizableStringsXml.py -h
Usage: LocalizableStringsXml.py [options]

Options:
  -h, --help            show this help message and exit
  -f filesDirectory, --filesDirectory=filesDirectory
                        StringsXml files directory.
  -t targetFilePath, --targetFilePath=targetFilePath
                        Target File (xls) Path.
```

#### Convert excel file to iOS & Android Localizable files.

```shell
python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx

$ python LocalizableBack.py -h
Usage: LocalizableBack.py [options]

Options:
  -h, --help            show this help message and exit
  -f filePath, --filePath=filePath
                        original.xls File Path.
  -t targetFloderPath, --targetFloderPath=targetFloderPath
                        Target Floder Path.
  -i iOSAdditional, --iOSAdditional=iOSAdditional
                        iOS additional info.
  -a androidAdditional, --androidAdditional=androidAdditional
                        android additional info.
```

#### Convert iOS Localizable.strings file to Android strings.xml file.

```shell
python Strings2Xml.py -f xxx/xxx.strings -t xxx/xxx.xml

python Strings2Xml.py -h
Usage: Strings2Xml.py [options]

Options:
  -h, --help            show this help message and exit
  -f filePath, --filePath=filePath
                        Localizable.strings File Path.
  -t targetFilePath, --targetFilePath=targetFilePath
                        Target File (strings.xml) Path.
  -a androidAdditional, --androidAdditional=androidAdditional
                        android additional info.
```

#### Extract strings to xls

```shell
python Strings2Xls.py -f xxx/xxx/ -t xxx/

$ python Strings2Xls.py -h
Usage: Strings2Xls.py [options]

Options:
  -h, --help            show this help message and exit
  -f filesDirectory, --filesDirectory=filesDirectory
                        Localizable.strings files directory.
  -t targetFilePath, --targetFilePath=targetFilePath
                        Target File (xls) Path.
```

#### Convert xls to strings

```shell
python Xls2Strings.py -f xxx/xxx -t xxx/

$ python Xls2Strings.py -h
Usage: Xls2Strings.py [options]

Options:
  -h, --help            show this help message and exit
  -f filePath, --filePath=filePath
                        original.xls File Path.
  -t targetFloderPath, --targetFloderPath=targetFloderPath
                        Target Floder Path.
  -i iOSAdditional, --iOSAdditional=iOSAdditional
                        iOS additional info.
  -a androidAdditional, --androidAdditional=androidAdditional
                        android additional info.
```

#### Convert iOS Project's all mult language \*.strings file to xls

```shell
python StringsAll2Xls.py -f xxx/xxx/ -t xxx/

$ python StringsAll2Xls.py -h
Usage: StringsAll2Xls.py [options]

Options:
  -h, --help            show this help message and exit
  -f filesDirectory, --filesDirectory=filesDirectory
                        Project files (strings) directory.
  -t targetDirectory, --targetDirectory=targetDirectory
                        Target files (xls) directory.
```

#### Reverse，Convert the xls content match to the origin strings files

```shell
python XlsMatch2Strings.py -f xxx/ -t xxx/xxx/

$ python XlsMatch2Strings.py -h
Usage: XlsMatch2Strings.py [options]

Options:
  -h, --help            show this help message and exit
  -f filePath, --filePath=filePath
                        original.xls File Path.
  -t targetFloderPath, --targetFloderPath=targetFloderPath
                        Target Floder Path.
```

## Thanks

- [Buguibu](https://github.com/buguibu)
