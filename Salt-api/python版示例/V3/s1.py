#coding:utf8
import json
import urllib
import urllib2

 #在python2.6x中，以下两行不是必须的
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url='https://192.168.2.101:8888'  #salt-api所在的“坐标”

def test():
  pre_data = [{"client":"local", "tgt":"*", "fun":"test.ping"}]   #根据上面官方文档的要求组成数组嵌套字典的形式
  json_data = json.dumps(pre_data)    #将其转化为json格式

  header = {"Content-Type":"application/json", "Accept":"application/json", "X-Auth-Token":"a3493c4e51cf7751097f1460014873384b69e9b5"}

  #这里说明下，Content-Type是声明传递给API的数据是什么格式的，这里指定了json，是因为上面的pre_data数据被我转化成了json格式
  #Accept是声明返回结果以什么样的格式显示，这里也指定了json格式来显示返回结果

  request = urllib2.Request(url, json_data, header)    #构造一次请求
  response = urllib2.urlopen(request)    #构造一次HTTP访问

  html = response.read()
  print html


if __name__=="__main__":
  test()