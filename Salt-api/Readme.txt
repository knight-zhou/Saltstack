�ο���
http://www.xiaomastack.com/2014/11/18/salt-api/

��ʼǰҲ��Ҫ��װsalt��api
yum install -y salt-api python-cherrypy

֤�����ɣ�
useradd -M -s /sbin/nologin saltapi
passwd saltapi
cd /etc/pki/tls/certs/
make testcert
һ·�س�
cd /etc/pki/tls/private/
openssl rsa -in localhost.key -out localhost_nopass.key


����salt�������ļ��뿴Ŀ¼�µ�:
master
master.d 

�Ƽ���װ��
ipython��

wget https://cloud.github.com/downloads/ipython/ipython/ipython-0.13.tar.gz
tar xzf ...
python setup.py install


������䣺
curl -k https://192.168.0.197:8888/login -H "Accept: application/x-yaml" -d username='saltapi' -d password='password' -d eauth='pam'