# -*- coding: utf-8 -*-
__time__ = '2018/3/5 16:07'
__author__ = 'winkyi@163.com'

import pika

class RabbitMQ(object):
    def __init__(self,username,password,ipaddr,port,vhost):
        credentials = pika.PlainCredentials(username,password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(ipaddr,port,vhost,credentials))
        self.channel = self.connection.channel()

    def __del__(self):
        self.connection.close()

    def sendMessage(self,queue_name,message):
        self.channel.queue_declare(queue_name)
        self.channel.basic_publish(
            exchange = '',
            routing_key=queue_name,  #queue名字
            body = message #消息内容
        )

if __name__ == '__main__':
    #conf配置文件的相关
    cf = GetConf("rbq.conf","main")
    ipaddr =  cf.get("host")
    port =  cf.getInt("port")
    username = cf.get('username')
    password = cf.get('password')
    vhost = cf.get('vhost')

    mq = RabbitMQ(username,password,ipaddr,port,vhost)
    mq.sendMessage('test','okokok')
