#coding=utf8
import os
import encrypt
import sys
import binascii

stdin_encoding =  sys.stdin.encoding
stdout_encoding = sys.stdout.encoding

def console_input():
    source_file_path = None
    secret = None
    prompt1 = "需要解密的文件(输入'exit'退出):"
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
        path_struct = os.path.split(source_file_path)
        file_parent_path = path_struct[0]
        file_name = path_struct[1]
        print file_name
        print file_parent_path
    
        secret = input_content
        key = encrypt.fillZero(secret)
        decypted_file_name = encrypt.decryptText(binascii.a2b_hex(file_name), key, encrypt.param)
        print decypted_file_name
        #当前目录
        if len(file_parent_path) == 0:
            decypted_file_path = decypted_file_name
        else:
            decypted_file_path = (r'%s\%s')%(file_parent_path,decypted_file_name)
        break
    
    encrypt.decryptFile(source_file_path, decypted_file_path, key, encrypt.param)
  
input_content = console_input()
