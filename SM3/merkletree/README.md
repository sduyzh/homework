Project: impl Merkle Tree following RFC6962

1.优化默克尔树数据结构
由于需要叶保存的是字符串，所以往结构体中新增字符串指针
![截图20220731110302](https://user-images.githubusercontent.com/110313650/182008018-542e589c-bca9-4799-8472-50902bd6a801.png)

结构体初始化 str 指向的是 NULL
![截图20220731110348](https://user-images.githubusercontent.com/110313650/182008013-ec04d5df-b7ca-48fc-b7e2-024b1c87ccc4.png)

2.实现字符串的哈希值简单计算
有关字符串的哈希值计，只有在子节点为叶子节点的节点中。其余的节点，还是计算两个整数。

![截图20220731110457](https://user-images.githubusercontent.com/110313650/182008049-2e5b10cb-66d2-4938-8fa4-d58cdf3e7949.png)

3.实现字符串的动态切割，分割为小的词组
在该函数中，切割字符串是以标点 或者 小词组为依据的

![截图20220731110603](https://user-images.githubusercontent.com/110313650/182008077-babf1a2d-330a-4c20-954e-43849012f167.png)

结果截图：
![截图20220731105444](https://user-images.githubusercontent.com/110313650/182008083-6652fc6b-97b0-4d7c-8a5f-e2e53492a0b4.png)
![截图20220731105507](https://user-images.githubusercontent.com/110313650/182008087-72c8073a-7ad4-41d1-86fd-69d886690a91.png)


