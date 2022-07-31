Project: survey of GCM,nonce reuse resistant GCM - SIV·Survey of TLS Weakness

GCM:

GCM可以提供对消息的加密和完整性校验，另外，它还可以提供附加消息的完整性校验。在实际应用场景中，有些信息是我们不需要保密，但信息的接收者需要确认它的真实性的，例如源IP，源端口，目的IP，IV，等等。因此，我们可以将这一部分作为附加消息加入到MAC值的计算当中。下图的Ek表示用对称秘钥k对输入做AES运算。最后，密文接收者会收到密文、IV（计数器CTR的初始值）、MAC值。

结果截图：
![截图20220731101323](https://user-images.githubusercontent.com/110313650/182006918-5effac00-e39c-4f12-8fb7-a7bfaa5e823c.png)
