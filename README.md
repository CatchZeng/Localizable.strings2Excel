## Localizable.strings2Excel
Python command line tool for conversion between iOS Localizable.strings and excel file & Localizable.strings to android strings.xml file.

[中文请点击](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/README-CN.md)

#### Convert iOS Localizable.strings files to excel.
![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  

#### Convert Android strings.xml files to excel.
![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/atox.jpg)

#### Convert excel file to iOS & Android Localizable files.
![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)

#### Convert iOS Localizable.strings file to Android strings.xml file.
![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg)


## ChangeLog

#### V0.5.0

1.Support convert Android strings.xml files to excel.

#### V0.4.0

1.Support convert multiple languages meanwhile.

#### V0.3.0

1.Support Localizable.strings to android strings.xml file.

#### V0.2.0 

1.Fix bugs.

2.Add -h(help command) for python files.

3.Add -t(target file path )、-f(source file path) configuration for python files.

#### V0.1.0 

Add project.


## Usage

### 1.install pyexcelerator component

change to pyexcelerator-0.6.4.1 directory,run ``` sudo python setup.py install ```

![install pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

### 2.install xld component

change to xlrd-1.0.0 directory,run ``` sudo python setup.py install ```


### 3.use python file
python Localizable.py -f xxx/xxx -t xxx/xxx.xls :convert iOS Localizable.strings files to xls file

![stoeu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoeu.jpg)


python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx  :convert xls file to iOS Localizable.strings files & Android strings.xml files

![etosu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etosu.jpg)


python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml : convert Localizable.strings to strings.xml file

![stoau](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoau.jpg)