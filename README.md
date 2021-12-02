# NLU文本自动化生成工具

## 一、Python及库文件版本
* Python 3.4及以上
* openpyxl==3.0.7
* pandas==1.0.0
* xlrd==2.0.1
* xlwt==1.3.0
## 二、快速开始
* 入口
```
python main.py
```
* 配置文件路径 
  * project/config
## 三、配置文件编写
* Category：表示该条指令的大类
* Module：表示该条指令的模块
* Feature：表示该条指令的功能点
* Query 
  * Q1#打开|关闭
  * Q2#迎宾音效
  * Q3#开关*          //这里的*表示开关是可选
* Domain
* Intent，包含打开的query,domain将被匹配为control_welcome_on
  * Q1#打开=control_welcome_on
  * Q2#关闭=control_welcome_off
* slot
  * 1.如果为Q1#打开={"name":"li"}，机制同intent
  * 2.如果为xx.txt, 代码会读取slot文件夹下的xx.txt作为匹配值。xx.txt的写法同样为打开|关闭={"name":"li"}
* 优先级
  * Q1#迎P0
* 车型，匹配到的车型，会在excel中划√, 否则x;当前仅支持D22,D55,E28,E38
  * Q1#D55
  * Q2#D22