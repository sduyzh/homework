#pragma once
#include <iostream>//��׼���������
#include <vector> 
#include <string> 
#include <fstream>
#include<sstream>
#include "BlockChain.h"
#include "sha256.h"
using namespace std;
class User
{
public:
	Blockchain uBlockchain;//��ǰ�ڵ㴴��һ���Լ�������������Ϊÿ���û�������һ���Լ���������
	string batchTX();//�������
};