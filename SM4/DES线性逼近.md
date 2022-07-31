Project: experimenting linear cryptanalysis of DES

S盒的线性分布：

定义：

​ ∑ i = 0 n < α , x > = x [ α i ] ⊕ x [ α i ] ⊕ . . . 

​ N S i ( α , β ) = ∣ { x ∣ 0 ≤ x ≤ 63 , ∑ i = 0 n < α , x > = ∑ i = 0 n < β , S i ( x ) > } ∣ 

其中，称 α 和 β 为掩码，在二进制层面比较好理解，假如α = 0011，x = 1110，那么< α , x > = 1 ⊕ 0 = 1
