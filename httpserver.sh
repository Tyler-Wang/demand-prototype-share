#!/bin/sh
docker run -it -d -p 8099:80 --name datahttpd -v 【httpd.conf文件】:/usr/local/apache2/conf/httpd.conf -v 【原型文件目录】:/usr/local/apache2/htdocs/ httpd
