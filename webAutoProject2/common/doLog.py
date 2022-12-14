#conding="utf-8"
#log类，处理log文件
import logging

from common import config


class Logger(object):
    #name是其他py文件的名称,WARNING默认等级(常量)
    def __init__(self,name,fileLevel=logging.WARNING):
        #定义记录器，日志对象，日志文件的实例
        self.logger=logging.Logger(name)
        #定义日志输出等级
        self.logger.setLevel(fileLevel)

        #格式化日志模板
        # fms = '%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s'  #指定什么样的格式
        # fmt=logging.Formatter(fms)#转化为指定格式
        fmt = logging.Formatter\
            ('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        #处理器，写信息到日志文件
        # 换成cur_date保证一天生成一个日志，在原来基础上追加和打印（动态的）
        logname=config.log_path+config.cur_date+".log"
        print(logname)
        #默认了一个mode="a"可追加的模式
        fh=logging.FileHandler(logname,encoding="utf-8")
        #设置下要让处理器按照什么格式书写日志------定义好的格式去写
        fh.setFormatter(fmt)
        #将处理器加入记录器中，让处理器在处理谁------就是让处理器给谁干活
        self.logger.addHandler(fh)

if __name__ == '__main__':
    #实例化log日志对象----等级传入什么，就出现等级及以上的错误信息/不传入，就输出初始化默认的等级及以上的信息
    logger=Logger(__name__,logging.DEBUG)
    #写日志
    #logging.DEBUG=10
    # logging.INFO=20
    # logging.WARNING=30
    # logging.ERROR=40
    # logging.CRITICAL=50
    #写debug级别的日志，等级10
    # logger.logger.log(logging.DEBUG,"我是debug级别的日志，等级是10")
    # #写info级别的日志，等级20
    # logger.logger.log(logging.INFO,"我是info级别的日志，等级是20")
    # #写info级别的日志，等级20
    # logger.logger.log(logging.WARNING,"我是waring级别的日志，等级是30")
    # # 写error级别的日志，等级20
    # logger.logger.log(logging.ERROR,"我是error级别的日志，等级是40")
    # # 写critical级别的日志，等级20
    # logger.logger.log(logging.CRITICAL,"我是critical级别的日志，等级是50")
    logger.logger.debug("我是debug级别的日志，等级是10")
    logger.logger.info("我是info级别的日志，等级是20")
    logger.logger.warning("我是waring级别的日志，等级是30")
    logger.logger.error("我是error级别的日志，等级是40")
    logger.logger.critical("我是critical级别的日志，等级是50")


































































