Project: do your best to optimize SM3 implementation

改进：

1.统一用array数组作为中间值，最大限度减少bytes、list、int之间的类型转换。

2.运算中经常用到"& 0xffffffff"确保值是32位，因为我们的计算机是64位，有时让中间值超过32位也无妨，仅在最后赋值时再进行"& 0xffffffff"运算，这样可减少运算量。但连续两次循环移位之间不能省略"& 0xffffffff"，否则会得到错误结果。

3.将循环移位运算从pysmx的“一次模除、一次乘法、一次加法”调整为“两次移位、一次按位或”，位运算比乘除法快。

结果截图：
![截图20220731084624](https://user-images.githubusercontent.com/110313650/182005658-eb9f5c37-3a10-4993-841c-bd58995f0d85.png)

注：pysmx库是从网上下的，也放在SM3里了
