tasks.py  最简单的使用方法
    celery -A tasks worker --loglevel=info

proj  以一个包的方式使用
    celery -A proj worker -l info

pro_celery  在django项目中使用
    https://www.cnblogs.com/alex3714/p/6351797.html
    http://www.jianshu.com/p/7a869a73b92f
    http://python.jobbole.com/81953/
    进入pro_celery项目目录： celery -A pro_celery worker -l info
