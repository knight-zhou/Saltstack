import json
import urllib
import urllib2

 #��python2.6x�У��������в��Ǳ����
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

url='https://192.168.2.101:8888'  #salt-api���ڵġ����ꡱ

def test():
  pre_data = [{"client":"local", "tgt":"*", "fun":"test.ping"}]   #��������ٷ��ĵ���Ҫ���������Ƕ���ֵ����ʽ
  json_data = json.dumps(pre_data)    #����ת��Ϊjson��ʽ
  
  header = {"Content-Type":"application/json", "Accept":"application/json", "X-Auth-Token":"a3493c4e51cf7751097f1460014873384b69e9b5"}
  #����˵���£�Content-Type���������ݸ�API��������ʲô��ʽ�ģ�����ָ����json������Ϊ�����pre_data���ݱ���ת������json��ʽ
  #Accept���������ؽ����ʲô���ĸ�ʽ��ʾ������Ҳָ����json��ʽ����ʾ���ؽ��

  request = urllib2.Request(url, json_data, header)    #����һ������
  response = urllib2.urlopen(request)    #����һ��HTTP����

  html = response.read()
  print html


if __name__=="__main__":
  test()