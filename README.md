# demand-prototype-share
自建需求原型分享工具

## 环境需求

- gogs
- 有docker和python3环境的服务器

## 搭建步骤

1. 修改demand-webhook-httpserver.py文件的HOST和GIT_URL

2. python3环境的服务器创建1个目录，如/usr/local/demand-prototype-share，在目录里面创建python虚拟环境：python3 -m venv .

3. 将demand-webhook-httpserver.py文件放到上面创建的目录，并在目录下通过./bin/pip install GitPython 安装依赖

4. 运行demand-webhook-httpserver.py，命令nohup /usr/local/demand-prototype-share/bin/python -u /usr/local/demand-prototype-share/demand-webhook-httpserver.py > /usr/local/demand-prototype-share/hook.log 2>&1 &

5. docker pull httpd拉取httpd镜像

6. 将httpd.conf文件放到服务器

7. 启动httpd，命令docker run -it -d -p 8099:80 --name datahttpd -v 【httpd.conf文件】:/usr/local/apache2/conf/httpd.conf -v 【原型文件目录】:/usr/local/apache2/htdocs/ httpd

8. 在gogs上原型仓库，仓库设置 -> 管理Web钩子 -> 添加Web钩子。录入http://服务器IP:8991

9. push更新到原型仓库

10. 使用浏览器，通过地址http:///服务器IP:8099访问原型页面
