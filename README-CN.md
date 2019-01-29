## Localizable.strings2Excel

iOS 本地化文件（Localizable.strings）与 Excel 互相转换 & Localizable.strings 转换成 android 的 strings.xml 文件的 Python 脚本工具

#### 将 iOS 多个国家的 Localizable.strings 转换成 excel

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)

#### 将 Android 多个国家的 strings.xml 转换成 excel

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/atox.jpg)

#### 将 excel 转换成 iOS 多个国家的 Localizable.strings 以及 Android 的 strings.xml

![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)

#### 将单个 iOS 的 Localizable.strings 转换成 Android 的 strings.xml

![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg)

#### 将 iOS 多个国家的 Localizable.strings 转换成多个 excel 文件

![extract strings to xls](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/strings2xls.jpg)

#### 将多个 excel 文件转换成 iOS 多个国家的 Localizable.strings

![convert xls to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/xls2strings.jpg)

## ChangeLog

[ChangeLog](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/CHANGELOG-CN.md)

## 使用方法

### 1.安装 pyexcelerator 组件

切换到 pyexcelerator-0.6.4.1 目录,执行 sudo python setup.py install 安装

![安装pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

### 2.安装 xld 组件

切换到 xlrd-1.0.0 目录,执行 sudo python setup.py install 安装

### 3.使用脚本

#### 将 iOS 多个国家的 Localizable.strings 转换成 excel

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

#### 将 Android 多个国家的 strings.xml 转换成 excel

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

#### 将 excel 转换成 iOS 多个国家的 Localizable.strings 以及 Android 的 strings.xml

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

#### 将单个 iOS 的 Localizable.strings 转换成 Android 的 strings.xml

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

#### 将 iOS 多个国家的 Localizable.strings 转换成多个 excel 文件

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

#### 将多个 excel 文件转换成 iOS 多个国家的 Localizable.strings

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

#### 将 iOS 项目多语言中的所有\*.strings 转换成对应的多个 excel 文件

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

#### 反转，将转出的 excel 文件内容替换回原先的 strings 文件中

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

## 鸣谢

- [Buguibu](https://github.com/buguibu)
