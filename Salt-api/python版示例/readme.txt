�ο���
https://docs.saltstack.com/en/latest/ref/clients/


����salt�ķ��ʣ�����ʹ��salt��api�ӿ� ��ȻҲ����ʹ��
salt.client

>>> import salt.client
>>> client = salt.client.LocalClient()
>>> ret = client.cmd('*','test.ping')
>>> ret
{'192.168.2.92': True}
