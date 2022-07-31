#include"Blockchain.h"
Blockchain::Blockchain()
{
	_vChain.emplace_back(Block(0, "Genesis Block"));
	_nDifficulty = 4;//�Ѷ�ֵ����3��������������4���Կ�����࣬5��ԼҪ��2�������ҡ�
}
void Blockchain::AddBlock(Block bNew)
{
	bNew.sPrevHash = _GetLastBlock().GetHash();
	bNew.MineBlock(_nDifficulty);
	_vChain.push_back(bNew);
	bNew.WriteBlcokToTXT();//�����������е�д�ļ�����
}

Block Blockchain::_GetLastBlock() const
{
	return _vChain.back();
}