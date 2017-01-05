## Localizable.strings2Excel
Python command line tool for conversion between iOS Localizable.strings and excel file & Localizable.strings to android strings.xml file.

中文请下翻

#### Convert iOS Localizable.strings files to excel.
![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  

#### Convert excel file to iOS & Android Localizable files.
![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)

#### Convert iOS Localizable.strings file to Android strings.xml file.
![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg)


## ChangeLog

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

###1.install pyexcelerator component

change to pyexcelerator-0.6.4.1 directory,run ``` sudo python setup.py install ```

![install pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

###2.install xld component

change to xlrd-1.0.0 directory,run ``` sudo python setup.py install ```


###3.use python file
python Localizable.py -f xxx/xxx -t xxx/xxx.xls :convert iOS Localizable.strings files to xls file

![stoeu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoeu.jpg)


python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx  :convert xls file to iOS Localizable.strings files & Android strings.xml files

![etosu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etosu.jpg)


python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml : convert Localizable.strings to strings.xml file

![stoau](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoau.jpg)

----

## Localizable.strings2Excel
iOS本地化文件（Localizable.strings）与Excel互相转换 & Localizable.strings 转换成android的strings.xml文件的Python脚本工具

#### 将iOS多个国家的Localizable.strings转换成excel
![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  

#### 将excel转换成iOS多个国家的Localizable.strings以及Android的strings.xml
![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg) 

#### 将单个iOS的Localizable.strings转换成Android的strings.xml
![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg) 

## ChangeLog

#### V0.4.0

1.支持多种语言一起转换

#### V0.3.0

1.支持Localizable.strings转换成android的strings.xml.

#### V0.2.0 

1.Fix bugs.

2.增加 -h(帮助命令)

3.增加 -t(目标文件地址)、-f(源文件地址)的命令参数

#### V0.1.0 

加入工程

## 使用方法

###1.安装pyexcelerator组件

切换到pyexcelerator-0.6.4.1目录,执行sudo python setup.py install 安装

![安装pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)


###2.安装xld组件

切换到xlrd-1.0.0目录,执行sudo python setup.py install 安装

###3.使用脚本

python Localizable.py -f xxx/xxx -t xxx/xxx.xls :将多个国家的iOS Localizable.strings文件一起转换成xls文件

![stoeu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoeu.jpg)

python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx  :将xls文件转换成多个国家Localizable.strings文件 & Android 多个国家的strings.xml文件

![etosu](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etosu.jpg)

python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml : 将单个Localizable.strings转换成strings.xml文件

![stoau](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoau.jpg)
