�ο���
https://docs.saltstack.com/en/latest/ref/clients/


����salt�ķ��ʣ�����ʹ��salt��api�ӿ� ��ȻҲ����ʹ��(�ǳ����㣬����ԭ����python2.6.6,ǧ��Ҫ������python2.7��Ȼ��website����python2.7�������ܲ�����)
salt.client

>>> import salt.client
>>> client = salt.client.LocalClient()
>>> ret = client.cmd('*','test.ping')
>>> ret
{'192.168.2.92': True}
