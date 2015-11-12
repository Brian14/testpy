__author__ = 'bao'

# import pexpect
from pexpect import popen_spawn
#     # from popen_spawn
# import sys
# # child = pexpect.fdpexpect.fdspawn('ssh hklxdv60')
child = popen_spawn.PopenSpawn('ls')
child.send('ssss')
# # child = pexpect.spawn(foo)
# child.logfile = sys.stdout
#
# # child.logfile = sys.stdout
# for line in sys.stdout:
#     print line.strip('\n')
print child.after