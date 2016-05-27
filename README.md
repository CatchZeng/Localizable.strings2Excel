## 简介
iOS本地化字符串与Excel互转的Python脚本工具

![strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/strings.jpg)   =>   ![excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/excel.jpg) 


![excel](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/excelback.jpg)   =>   ![strings](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/stringsback.jpg) 


## 使用方法

###1.安装pyexcelerator组件

切换到pyexcelerator-0.6.4.1目录,执行sudo python setup.py install 安装

![安装pyexcelerator](https://github.com/CatchZeng/Localizable.strings2Excel/blob/master/imgs/installpy.jpg)

###2.使用脚本
python Localizable.py  ：把Localizable.strings中的所有key值填到Localizable.xls中

python LocalizableBack.py  ：把LocalizableBack.xls中的所有值回填到LocalizableBack.strings中

或安装pycharm ce IDE环境运行