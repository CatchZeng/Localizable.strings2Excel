## 简介
将iOS和js的本地化字符串与Excel互转的Python脚本工具

## 使用方法

###1.安装pyexcelerator组件

切换到pyexcelerator-0.6.4.1目录,执行sudo python setup.py install 安装

###2.使用脚本
python Localizable.py  ：把Localizable.strings中的所有key值填到Localizable.xls中

python LocalizableBack.py  ：把LocalizableBack.xls中的所有值回填到LocalizableBack.strings中

python JSLocalizable.py  ：把en.js中的所有key值填到JSLocalizable.xls中

python JSLocalizableBack.py  ：把JSLocalizableBack.xls中的所有值回填到JSLocalizableBack.js中

或安装pycharm ce IDE环境运行