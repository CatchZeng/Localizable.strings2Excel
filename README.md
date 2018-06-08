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

## Usage

### 1.install pyexcelerator component

change to pyexcelerator-0.6.4.1 directory,run ``` sudo python setup.py install ```

![install pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

### 2.install xld component

change to xlrd-1.0.0 directory,run ``` sudo python setup.py install ```


### 3.use python file

#### Convert iOS Localizable.strings files to excel.

```python
python Localizable.py -f xxx/xxx -t xxx/xxx.xls
```

![stoeu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoeu.jpg)

#### Convert Android strings.xml files to excel.

```python
python LocalizableStringsXml.py -f xxx/xxx -t xxx/xxx.xls
```

![xmltoe](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/xmltoe.jpg)

#### Convert excel file to iOS & Android Localizable files.

```python
python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx
```

![etosu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etosu.jpg)

#### Convert iOS Localizable.strings file to Android strings.xml file.

```python
python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml
```

![stoau](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoau.jpg)

#### Extract strings to xls

```python
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

```python
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

## Thanks

- [Buguibu](https://github.com/buguibu)
