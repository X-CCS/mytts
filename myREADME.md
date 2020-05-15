+[Ossian](https://github.com/CSTR-Edinburgh/Ossian)
git clone https://github.com/CSTR-Edinburgh/Ossian.git


nginx version: nginx/1.10.3 (Ubuntu)

ssh root@192.168.9.202 
123456

source activate /home/chenchangshu/.conda/envs/Django_Can_py37
cd /home/chenchangshu/mytts
cp -r ./mytts /etc/nginx/sites-available/

sudo ln -s ./mytts /etc/nginx/sites-enabled

copy ./unicorn/mytts to /etc/nginx/sites-available/ test it enable site

python manage.py runserver 0.0.0.0:8001

python manage.py runserver 0.0.0.0:8001 
sudo lsof -t -i tcp:8001 | xargs kill -9

http://0.0.0.0:8001/

+ [Django 浏览器打开警告Not Found: /favicon.ico](https://blog.csdn.net/u013251992/article/details/77855956)

查看django的安装路径

pip show django

/home/chenchangshu/.conda/envs/Django_Can_py37/lib/python3.7/site-packages

/home/chenchangshu/.conda/envs/Django_Can_py37/lib/python3.7/site-packages/django/contrib/admin/static/admin/img/favicon.ico
/home/chenchangshu/.conda/envs/Django_Can_py37/lib/python3.7/site-packages/django/__init__.py
http://192.168.9.202:8001/test

export PATH=$PATH:/home/chenchangshu/mytts
http://192.168.9.202:8001/trans

"POST / HTTP/1.1" 400 18

测试接口正常连接：http://192.168.9.202:8001/test get 可以 post不行
http://192.168.9.202:8001/trans