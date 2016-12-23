## Localizable.strings2Excel
Python command line tool for conversion between iOS Localizable.strings and excel file & Localizable.strings to android strings.xml file.

中文请下翻

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  

![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)

![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg)


## ChangeLog

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

###2.use python file
python Localizable.py -f xxx/xxx.strings -t xxx/xxx.xls :convert Localizable.strings to xls file

python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx.strings  :convert xls file to Localizable.strings file

python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml : convert Localizable.strings to strings.xml file

----

## Localizable.strings2Excel
iOS本地化文件（Localizable.strings）与Excel互相转换 & Localizable.strings 转换成android的strings.xml文件的Python脚本工具

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  

![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg) 

![strings to android xml](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stox.jpg) 

## ChangeLog

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

###2.使用脚本
python Localizable.py -f xxx/xxx.strings -t xxx/xxx.xls  ：把Localizable.strings转换成xls文件

python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx.strings  ：把xls文件转换成Localizable.strings文件

python LocalizableToStringXml.py -f xxx/xxx.strings -t xxx/xxx.xml : 将 Localizable.strings转换成strings.xml文件
