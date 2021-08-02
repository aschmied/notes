# Networking

* Watch the UDP input queue: `netstat -c --udp -an`
* Check for dropped UDP packets: `cat /proc/net/udp`
* Add route. Route traffic for the 10.2 subnet to the gateway at 10.11.99.100: `sudo route add -net 10.2.0.0 netmask 255.255.0.0 gw 10.11.99.100`
* Delete route: sudo route del -net 10.2.0.0 netmask 255.255.0.0
* List open ports and processes attached to them: `netstat -a -b`
* Dump UDP on port 10.11.1.2: `tcpdump -i eth0 -s 0 -v host 10.11.1.2 and udp`
* Watch the SSL handshake using OpenSSL. Can be useful for debugging cert problems: `openssl s_client -connect host:port`
* Dump incoming traffic on tcp port 1234: `sudo tcpflow -i any -C -J port 1234`
* Throttle HTTP for testing on Windows: http://jagt.github.io/clumsy/index.html
