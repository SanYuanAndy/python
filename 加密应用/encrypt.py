#coding=utf8
from Crypto.Cipher import AES
import os

def fillZero(data):
    data_len = len(data)
    fill_len = 16 - (data_len %16)
    if fill_len != 16:
        for i in range(0, fill_len):
            data += '\0'
    return data

def removeZero(data):
    while True:
        data_len = len(data)
        if data_len == 0 or data[data_len - 1] != '\0':
            break
        data = data[0:data_len - 1]
    return data

class CWorker:
    def __init__(self, sKey, sParam):
        self.key = sKey
        self.param = sParam
        self.aes = AES.new(self.key, AES.MODE_CBC, self.param)
    def work(self, data, tail):
        pass
    def AESObj(self):
        return self.aes

class CEncrypter(CWorker):
    def __init__(self, sKey, sParam):
        self.name = "encrypter"
        CWorker.__init__(self,sKey, sParam)
    def work(self, data, tail):
        return CWorker.AESObj(self).encrypt(fillZero(data))

class CDecrypter(CWorker):
    def __init__(self, sKey, sParam):
        self.name = "descrypter"
        CWorker.__init__(self,sKey, sParam)
    def work(self, data, tail):
        if tail:
            return removeZero(CWorker.AESObj(self).decrypt(data))
        else:
            return CWorker.AESObj(self).decrypt(data)
        
param = '1234561234561234'

def encryptText(plainText, key, param):
    worker = CEncrypter(key, param)
    return worker.work(plainText, True)

def decryptText(decryptedText, key, param):
    worker = CDecrypter(key, param)
    return worker.work(decryptedText, True)

def encryptFile(source_file_name, target_file_name, key, param):
    worker = CEncrypter(key, param)
    do_work(source_file_name, target_file_name, worker)

def decryptFile(source_file_name, target_file_name, key, param):
    worker = CDecrypter(key, param)
    do_work(source_file_name, target_file_name, worker)

def do_work(source_file_name, target_file_name, worker):
    source_file_object = None
    target_file_obj = None
    source_file_size = None
    tail = False
    try:
        source_file_size = os.path.getsize(source_file_name)
        source_file_object = open(source_file_name, 'rb')
        target_file_obj = open(target_file_name, 'wb')
        while True:
            data = source_file_object.read(16*64)
            #print len(data)
            if not data:
                print 'file arrive end'
                break
            source_file_size = source_file_size - len(data)
            if source_file_size <= 0:
                tail = True
            target_file_obj.write(worker.work(data, tail))
            
    except Exception, e:
        print e

    if source_file_object:
        source_file_object.close()
    if target_file_obj:
        target_file_obj.close()

 


    
