#pragma once
#pragma once
#include"Block.h"
#include<vector>//������
class Blockchain
{
public:
	Blockchain();//Ĭ�Ϲ��캯��
	void AddBlock(Block bNew);//�������麯��
	uint32_t _nDifficulty;//�Ѷ�ֵ
	vector<Block> _vChain;//��������ı���
	Block _GetLastBlock() const;//��ȡ���µ����飬��const�ؼ��֣���ʾ��������ݲ��ɸ���
};