from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES
 
# 密钥在使用该方法时可补足为16倍数
# 偏移量在使用该方法时，在不足16位时补为16位
# 偏移量必须为16位，不可多
def legth(value):
    l = len(value)
    flag = l % 16
    if flag != 0:
        add = 16 - (l % 16)
        value = value + ('\0' * add).encode('utf-8')
    return value
 
 
def encryp_str(content, key, mode, iv):
    cryptor = AES.new(key, mode, iv)
    # 被加密内容需大于密钥长度,且为16倍数
    key_length = len(key)
    content_legth = len(content)
    if content_legth < key_length:
        add = key_length - content_legth
        content = content + ('\0' * add).encode('utf-8')
    elif content_legth > key_length:
        add = 16 - (content_legth % 16)
        content = content + ('\0' * add).encode('utf-8')
    cipher_content = cryptor.encrypt(content)  # 加密
    print('加密1：', cipher_content)
    cipher_content_hex = b2a_hex(cipher_content)
    print('加密2：', cipher_content_hex)
    cipher_content_hex_de = cipher_content_hex.decode()
    print('密文：', cipher_content_hex_de)
    return cipher_content_hex_de
 
 
def decryp_str(en_content, key, mode, iv):
    cryptor = AES.new(key, mode, iv)
    content = a2b_hex(en_content)
    print('解密1：', content)
    content = cryptor.decrypt(content)
    print('解密2：', content)
    content = bytes.decode(content).rstrip('\0')
    print('明文：', content)
    return content
 
 
if __name__ == '__main__':
    # 加密内容
    content = input('输入加密内容：')
    # 密钥
    key = input('输入密钥：')
    key = key.encode('utf-8')  # 密钥需编码
    # 偏移量
    iv = input(r'输入偏移量（16位），少于16位将使用“\0”自动补齐：')
    print('原文：', content)
    content = content.encode('utf-8')  # 编码加密内容
    iv = iv.encode('utf-8')
    # 处理key和iv长度
    key = legth(key)
    iv = legth(iv)
 
    mode = AES.MODE_CBC  # 加密模式
 
    en_content = encryp_str(content, key, mode, iv)
    content = decryp_str(en_content, key, mode, iv)
