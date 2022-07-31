Project: send a tx on Bitcoin testnet,and parse the tx data down to everybit,better write script yourself

Blockchain.h创建一个区块链类
![截图20220731083623](https://user-images.githubusercontent.com/110313650/182004866-46efc1ab-6a1c-4214-a710-1791314c7a6d.png)

Blockchain.cpp修改难度值改为4，可以看出差距
![截图20220731083714](https://user-images.githubusercontent.com/110313650/182004903-1fec39c3-fe7e-4148-a321-aa6c5f084d0b.png)

Block.h声明区块类，包含区块索引值，随机数，描述字符，Hash值，生成时间
![截图20220731083613](https://user-images.githubusercontent.com/110313650/182004860-b7fd9b8c-33e4-4fc7-b459-996572b5179e.png)

Block.cpp记录时间，将输出数据保存到文档中
![截图20220731083651](https://user-images.githubusercontent.com/110313650/182004883-cf3d2da4-b469-42cd-aa62-437c3070fc7e.png)

sha256.h 和sha256.cpp均为需要使用的函数，直接网上摘抄即可

user.h创建一个用户类

![截图20220731083635](https://user-images.githubusercontent.com/110313650/182004829-19f074f8-4e2b-4efd-9eb6-d310a1a9c326.png)

user.cpp这里是实现用户的打包交易，通过默克尔树的方式将若干条交易打包
![截图20220731083747](https://user-images.githubusercontent.com/110313650/182004891-8c5b5e2b-cb82-42f6-bff3-79de6e22b7aa.png)

TestforBitcoin.cpp这就是测试程序了，假设100个用户中某个用户挖矿成功了，然后来挖矿
![截图20220731083723](https://user-images.githubusercontent.com/110313650/182004893-858108bc-8f25-4af8-9946-cce6c7a3fa8d.png)

结果截图：
![截图20220731083157](https://user-images.githubusercontent.com/110313650/182004670-eb1d2e3f-207f-487f-b4c6-959c14f62e0e.png)
