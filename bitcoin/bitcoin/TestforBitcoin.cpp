#include<iostream>
#include<cstdint>
#include"Blockchain.h"
#include"user.h"
#include<stdio.h>
#include <cstdlib>
#include <ctime>
#include"time.h"
#include"sha256.h"
using namespace std;
int main()
{
	srand((int)time(0));//���������
	Blockchain bChain = Blockchain();//���ȴ���һ��������
	User user[100];//����100���û�
	int miner_id;
	for (int i = 0; i < 100000; i++)//ʮ��γ��飬��¼�����ٶ�
	{
		miner_id = rand() % 100;
		for (int j = 0; j < 100; j++)
		{
			user[j].uBlockchain = bChain;//��100���ڵ����������ʼ����
		}
		user[miner_id].uBlockchain = bChain;//���ڿ������ʼ��
		printf("Mining block  %d...\n", i);
		user[miner_id].uBlockchain.AddBlock(Block(i, user[miner_id].batchTX()));
		bChain = user[miner_id].uBlockchain;
		printf("Miner ID is %d...\n", miner_id);
	}
	system("pause");
	return 0;
}