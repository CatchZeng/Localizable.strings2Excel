## Localizable.strings2Excel
iOS本地化文件（Localizable.strings）与Excel互相转换 & Localizable.strings 转换成android的strings.xml文件的Python脚本工具

#### 将iOS多个国家的Localizable.strings转换成excel
![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  

#### 将Android多个国家的strings.xml转换成excel
![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/atox.jpg)  

#### 将excel转换成iOS多个国家的Localizable.strings以及Android的strings.xml
![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg) 

#### 将单个iOS的Localizable.strings转换成Android的strings.xml
![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg) 

#### 将iOS多个国家的Localizable.strings转换成多个excel文件
![extract strings to xls](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/strings2xls.jpg)

#### 将多个excel文件转换成iOS多个国家的Localizable.strings
![convert xls to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/xls2strings.jpg)

## ChangeLog

[ChangeLog](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/CHANGELOG-CN.md)

## 使用方法

### 1.安装pyexcelerator组件

切换到pyexcelerator-0.6.4.1目录,执行sudo python setup.py install 安装

![安装pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)


### 2.安装xld组件

切换到xlrd-1.0.0目录,执行sudo python setup.py install 安装

### 3.使用脚本

#### 将iOS多个国家的Localizable.strings转换成excel

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

#### 将Android多个国家的strings.xml转换成excel

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

#### 将excel转换成iOS多个国家的Localizable.strings以及Android的strings.xml

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

#### 将单个iOS的Localizable.strings转换成Android的strings.xml

```shell
python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml

python LocalizableToStringXml.py -h
Usage: LocalizableToStringXml.py [options]

Options:
  -h, --help            show this help message and exit
  -f filePath, --filePath=filePath
                        Localizable.strings File Path.
  -t targetFilePath, --targetFilePath=targetFilePath
                        Target File (strings.xml) Path.
  -a androidAdditional, --androidAdditional=androidAdditional
                        android additional info.
```


#### 将iOS多个国家的Localizable.strings转换成多个excel文件

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

#### 将多个excel文件转换成iOS多个国家的Localizable.strings

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

## 鸣谢

- [Buguibu](https://github.com/buguibu)