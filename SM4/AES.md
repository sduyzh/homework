Project: survey of AES implementatin software impl

1.预处理
AES有三种密钥长度16(*AES-128*), 24 (*AES-192*), 和 32 (*AES-256*)，在对字符进行加密时，密码和明文长度自动填充16位

2.加密
要调用PyCrypto的AES加密模块，首先导入AES的包，另外为了确保编码的统一，我选择将密文保存为16进制，因此还需要从binascii中导入b2a_hex和a2b_hex

3.解密
这里加解密使用的都是CBC模式,直接调用库函数即可

结果截图：
![截图20220731092500](https://user-images.githubusercontent.com/110313650/182005926-2bfafaca-415e-4db0-828b-628eb12be4bd.png)
