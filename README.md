## Localizable.strings2Excel
Python command line tool for conversion between iOS Localizable.strings and excel file.

中文请下翻

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  


![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)  

## ChangeLog

#### V0.2.0 
1.fix bugs
2.add -h(help command) for python files
3.add -t(target file path )、-f(source file path) configuration for python files

#### V0.1.0 
add project


## Usage

###1.install pyexcelerator component

change to pyexcelerator-0.6.4.1 directory,run ``` sudo python setup.py install ```

![install pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

###2.use python file
python Localizable.py -f xxx/xxx.strings -t xxx/xxx.xls ：exchange Localizable.strings to xls file

python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx.strings  ：exchange xls file to Localizable.strings file

## Localizable.strings2Excel
iOS本地化字符串与Excel互相转换的Python脚本工具

![strings to excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stoe.jpg)  


![excel to strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/etos.jpg)  


## 使用方法

###1.安装pyexcelerator组件

切换到pyexcelerator-0.6.4.1目录,执行sudo python setup.py install 安装

![安装pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

###2.使用脚本
python Localizable.py -f xxx/xxx.strings -t xxx/xxx.xls  ：把Localizable.strings转换成xls文件

python LocalizableBack.py -f xxx/xxx.xls -t xxx/xxx.strings  ：把xls文件转换成Localizable.strings文件
