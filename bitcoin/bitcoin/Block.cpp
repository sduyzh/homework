#include"Block.h"
#include"sha256.h"
#include"time.h"
#include<sstream>
Block::Block(uint32_t nIndexIn, const string& sDataIn) :_nIndex(nIndexIn), _sData(sDataIn)
//���캯��Block����������ΪnIndexIn��sDataIn���ֱ�ֵ��Block�е�_nIndex��_sData�����캯����ʼ���÷���
{
	_nNonce = -1;//Nounce����Ϊ-1
	_tTime = time(nullptr);//����ʱ��
	if (nIndexIn == 0)//�˴�����ʱ���¼������Ϊ�˼�¼��ǰ������������Ҫ��ʱ�䣬�����ǵ�ǰʱ��
		first_time = _tTime;
}
string Block::GetHash()//���ع�ϣֵ������ʵ��
{
	return _sHash;
}
void Block::MineBlock(uint32_t nDifficulty)//�ڿ���������Ϊ�Ѷ�ֵ��
{
	//char cstr[nDifficulty + 1];
	char cstr[10 + 1];//�������ʵ�������ö�󶼿��ԣ�����Ҫ����nDifficulty��ֵ
	for (uint32_t i = 0; i < nDifficulty; ++i)//������飬ʹ�����ǰnDifficultyλ��Ϊ0����Ϊ�Ѷȡ�
	{
		cstr[i] = '0';
	}
	cstr[nDifficulty] = '\0';
	string str(cstr);//����һ��string��Ķ��󣬳�ʼ��Ϊcstr�����ַ�������ת��Ϊstring�����

	do
	{
		_nNonce++;
		_sHash = _CalculateHash();

	} while (_sHash.substr(0, nDifficulty) != str);//substr��ʾ���±�0��ʼ--->nDifficulty������
	//ҪѰ��һ��Nounceʹ�������ϣֵ��ǰnλ��0����0�ĸ��������Ѷ�ֵ�ĸ�����ͬ�����ڿ�ɹ���
	cout << "Block mined:" << _sHash << endl;
}

inline string Block::_CalculateHash() const
{
	stringstream ss;//�ö������ͨ��<<���ն�����ݣ����浽ss�����У���ͨ��str�����������ݸ���һ��string����
	ss << _nIndex << _tTime << _sData << _nNonce << sPrevHash;
	//return sha256(ss.str());
	return sha256(sha256(ss.str()));
}

void Block::WriteBlcokToTXT()//�����ɵ��������������һ��txt�ĵ���������·���Լ���
{
	ofstream outfile("out.txt", ios::app);//�˴��޸ı����������ݵ�·��
	outfile << "Index:" << _nIndex << endl;
	outfile << "Nonce:" << _nNonce << endl;
	outfile << "_sData:" << _sData << endl;
	outfile << "_sHash:" << _sHash << endl;
	outfile << "sPrevHash:" << sPrevHash << endl;
	outfile << "_tTime:" << _tTime - first_time << endl;
	outfile << endl;
	outfile.close();
}