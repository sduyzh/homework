#include"user.h"
string User::batchTX()
{
    ifstream myfile("300TXdata.txt");//��ȡtxt�ĵ��е�300����������
    string temp[300];
    int i = 0;
    if (!myfile.is_open())
    {
        cout << "δ�ɹ����ļ�" << endl;
    }
    while (getline(myfile, temp[i++]))//��ȡ�����ĵ�һ�з���������i��λ��Ȼ��i++
    {
        //cout << temp[i++] << endl;
        getline(myfile, temp[i++]);//��ȡ��������һ�з�������i�����λ��Ȼ��i++
        //cout << temp[i] << endl;
    }

    for (int i = 0; i < 300; i++)//����һ��αĬ�˶������ɹ��̣�Ϊ�˱���ʵ�֣�������д�ˡ�
    //ʵ�������Ĭ�˶�������Ҳ���ѣ���ʱ�������ɡ�
    {
        stringstream ss;//�ö������ͨ��<<���ն�����ݣ����浽ss�����У���ͨ��str�����������ݸ���һ��string����
        ss << temp[0] << temp[i];
        temp[0] = sha256(ss.str());
        //cout << temp[0] << endl;
    }

    myfile.close();
    return temp[0];
}

