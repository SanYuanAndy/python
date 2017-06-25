#coding=utf8
import os
import encrypt
import sys
import binascii

stdin_encoding =  sys.stdin.encoding
stdout_encoding = sys.stdout.encoding

def console_input(output):
    if not os.path.exists(output):
        os.mkdir(output)
    
    source_file_path = None
    secret = None
    prompt1 = "需要加密的文件(输入'exit'退出):"
    prompt2 = "输入6-16位数字和字母组合密码(字母区分大小写,输入'exit'退出):"
    
    while True:
        input_content = raw_input(prompt1.decode('utf8').encode(stdin_encoding))
        if input_content == 'exit':
            return
        if len(input_content) == 0:
            print 'file path can not be empty'
            continue
        if not os.path.exists(input_content):
            print 'file do not exists'
            continue
        source_file_path = input_content
        break
    while True:
        input_content = raw_input(prompt2.decode('utf8').encode(stdin_encoding))
        if input_content == 'exit':
            return
        if len(input_content) < 6 or len(input_content) > 16:
            print 'secret length is not match'
            continue
        secret = input_content
        break
    path_struct = os.path.split(source_file_path)
    file_parent_path = path_struct[0]
    file_name = path_struct[1]
    print file_name
    print file_parent_path
    
    key = encrypt.fillZero(secret)
    encypted_file_name = binascii.b2a_hex(encrypt.encryptText(file_name, key, encrypt.param))
    print encypted_file_name
    encypted_file_path = (r"%s\%s")%(output, encypted_file_name)
    encrypt.encryptFile(source_file_path, encypted_file_path, key, encrypt.param)

input_content = console_input('output')
