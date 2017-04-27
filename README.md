sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install git
sudo apt-get install python2.7
sudo apt-get install python-pip
sudo apt-get install libjpeg-dev
sudo apt-get install python-dev libmysqlclient-dev
sudo apt-get install django-cleanup
sudo apt-get install mysql-server
mkdir /home/user
sudo git clone https://github.com/ramble9502/ramble9502.git
cd /home/user/ramble9502
pip install –r requirements.txt

mysql -u root -p
CREATE DATABASE <dbname> CHARACTER SET utf8;
(Database 的名稱帳號密碼與 mysite/mysite/settings.py 裡的 DATABASES必須吻合，需再更改)
python manage.py makemigraitons
python manage.py migrate 
python manage.py createsuperuser  
(創建帳號密碼  帳號：admin87932 密碼：47zX6h8cXc)
python mange.py migrate

sudo nano /etc/apache2/ennvars
更改內容-------export LANG="en_US.UTF-8"

python manage.py collecstatic

設定 apache
sudo vi /etc/apache2/sites-available/sitename.conf  #自行填寫
<VirtualHost *:80>
    ServerName www.yourdomain.com     #自行填寫
    ServerAlias otherdomain.com       #自行填寫
    ServerAdmin tuweizhong@163.com    #自行填寫
  
    Alias /media/ /home/user/ramble9502/mysite/media_cdn/
    Alias /static/ /home/user/ramble9502/mysite/static/
  
    <Directory /home/user/ramble9502/mysite/media_cdn>
        Require all granted
    </Directory>
  
    <Directory /home/user/ramble9502/mysite/static>
        Require all granted
    </Directory>
  
    WSGIScriptAlias / /home/user/ramble9502/mysite/mysite/wsgi.py
  
    <Directory /home/user/ramble9502/mysite/mysite>
    <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>
</VirtualHost>


cd /home/user/ramble9502/mysite/
sudo chgrp -R www-data media_cdn
sudo chmod -R g+w media_cdn
sudo chown -R www-data:www-data media_cdn



sudo a2ensite sitename 或 sudo a2ensite sitename.conf


