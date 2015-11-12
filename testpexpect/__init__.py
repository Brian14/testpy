__author__ = 'bao'

from  pxssh import pexpect
# 初始化pxssh示例
s = pxssh.pxssh()

hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
# 建立ssh连接
s.login(hostname, username, password)
# 发送命令到远程终端
s.sendline('uptime')  # run a command
# 等待远程终端返回
s.prompt()  # match the prompt
# 打印匹配到的内容
print s.before  # print everything before the propt.

# 发送命令到远程终端
s.sendline('ls -l')
# 等待远程终端返回
s.prompt()
# 打印匹配到的内容
print s.before

s.sendline('df')
s.prompt()
print s.before

# 释放ssh连接
s.logout()
