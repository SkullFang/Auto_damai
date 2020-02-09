# 前言

这是大麦网自动抢票软件，本人对前端知识不是很熟悉。fork了https://github.com/Entromorgan/Autoticket .做了以下修改

- 修改了配置 .json -> .py 利于理解与代码修改。
- 添加了loger，便于定位错误原因。
- 修改了部分代码，可以无限循环指定场次抢票（原项目也有这部分代码，但貌似是bug）
- 修改了chromedriver读取，免安装。

# 准备工作

## 下载依赖
```bash
pip install -r requirement.txt
``` 

## 下载chromedriver

step 1. 从[网站](https://chromedriver.chromium.org/downloads)下载与自己的chrome对应的chromedriver

这里给出版本对应[参考](https://blog.csdn.net/BinGISer/article/details/88559532)


step 2. 把文件放进根目录

# 修改配置文件
config.py

修改程序配置
```python
class FLAG:
    sess=[1,2,3] #场次
    price=[6] #票价等级
    date=0 #可以定时自动启动没实现
    real_name=[] #忽略
    nick_name="xxxx" #昵称 用于登陆校验
    ticket_num = 2 #购买票数
    base_url="https://www.damai.cn/"
    target_url="https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.68dcea2fF8qcVt&id=611305813172&clicktitle=JJ%20%E6%9E%97%E4%BF%8A%E6%9D%B0%E3%80%8A%E5%9C%A3%E6%89%80%EF%BC%9AWONDERLAND%E3%80%8B%E4%B8%96%E7%95%8C%E5%B7%A1%E5%9B%9E%E6%BC%94%E5%94%B1%E4%BC%9A%E2%80%94%E2%80%94%E4%B8%8A%E6%B5%B7%E7%AB%99"
    browse='Chrome'

```

修改 logger 配置 这部分默认。想折腾的也可以修改

# 运行

```bash
python Autoticket.py

```

注： 如果没有登陆过，会启动大麦网首页进行登陆并且生成cookies。下次运行直接读cookies，不需要重新登陆。但是cookies有一定时间限制
如果程序提示错误，可以手动删掉cookies文件，再次运行即可。


# 未实现&改进方向

- 订单支付页比较模糊，主要还是没有实际的case去尝试，本人上次抢到之后没钱支付cancel了。
- 全自动化登陆未实现，因为我直接是微信扫码登陆。
- 多线程多账号登陆未实现，应该可以大大提升抢票几率。

欢迎提issue