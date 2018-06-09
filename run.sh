外网：
  运行：
  python3 master.py -l 0.0.0.0:1081 -e 0.0.0.0:50067 -s nN31mnOq0ek4UBXxecl4WnLeCoYOfTQJ -t 120 --log-level DEBUG
  表示：(1)对于所有对本机1081端口的请求，均转发给连接到本机50067端口的机子上。
内网：
(1) 运行
  python server.py
  此时监听8080端口，对于任意HTTP请求，均返回<h1>success</h1>
  可以用浏览器访问此内网，检查网页打开是否正常。
(2)运行
  python slave.py -l 0.0.0.0:8080 -e 120.78.190.146:50067 -s nN31mnOq0ek4UBXxecl4WnLeCoYOfTQJ -t 120 --log-level DEBUG
  表示(1)连接外网IP 120.78.190.146 ，50067端口，并将外网数据全部转发给本机8080端口上。

说明：这样，最终在外网机子1081端口和内网机子8080端口之间建立一条隧道；所有发往外网1081端口的数据均会转发给内网8080端口。