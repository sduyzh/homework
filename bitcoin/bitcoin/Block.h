#pragma once
#include<cstdint>//������uint32_t���޷�������
#include<iostream>//��׼���������
#include <fstream>
using namespace std;
static time_t first_time = 0;//����ط���Ϊ�˼�¼ÿ��������������һ�������ʱ������õ�ȫ�ֱ���
//����������
class Block
{
public:
	string sPrevHash;//ǰһ������Ĺ�ϣֵ
	Block(uint32_t nIndexIn, const string& sDataIn);//���캯��
	string GetHash();//���ع�ϣֵ
	void MineBlock(uint32_t nDifficulty);//�ڿ������nDifficulty��ʾָ�����Ѷ�ֵ
	void NoMineBlock();//���ڿ�ֱ���������
	uint32_t _nIndex;//��������ֵ���ڼ������飬��0��ʼ����
	int64_t _nNonce;//���������
	string _sData;//���������ַ�
	string _sHash;//����Hashֵ
	time_t _tTime;//��������ʱ��
	string _CalculateHash() const;//����Hashֵ��const��֤����ĺ���ֵ���ܱ��ı䡣
	void WriteBlcokToTXT();//����������д�뵽TXT�ļ���
};