#coding=utf8
import re
#方式2每次match之前都编译了一次匹配规则，不论匹配规则是否发生了变化，效率没有方式1高
cmds = ['dir', 'COPY', 'Cd']

print '1'
pattern = re.compile(r'dir|copy|cd', re.I)
for cmd in cmds:
    print pattern.match(cmd)
print

print 2
for cmd in cmds:
    print re.match(r'dir|copy|cd', cmd, re.I)
