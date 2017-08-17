import socket
print 'create socket....'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'done'

print 'looking up port number.....'
port = socket.getservbyname('http','tcp')
print 'done'

print 'connect to remote host on port %d...' %port
s.connect(('www.baidu.com',port))
print 'done'