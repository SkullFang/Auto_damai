# coding: utf-8
import logging
from logging import handlers
class FLAG:
    sess=[1,2,3] #场次
    price=[6] #票价等级
    date=0
    real_name=[]
    nick_name="xiaohuahua954" #昵称 用于登陆校验，读cookies用
    ticket_num = 2
    base_url="https://www.damai.cn/"
    target_url="https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.68dcea2fF8qcVt&id=611305813172&clicktitle=JJ%20%E6%9E%97%E4%BF%8A%E6%9D%B0%E3%80%8A%E5%9C%A3%E6%89%80%EF%BC%9AWONDERLAND%E3%80%8B%E4%B8%96%E7%95%8C%E5%B7%A1%E5%9B%9E%E6%BC%94%E5%94%B1%E4%BC%9A%E2%80%94%E2%80%94%E4%B8%8A%E6%B5%B7%E7%AB%99"
    browse='Chrome'


class LOG:


    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射


    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)



