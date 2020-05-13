#include <iostream>

using namespace std;
int main()
{
	int N, cnt = 0;
	cin >> N;
	int i = 666, temp;
	bool flag;

	while (cnt != N)
	{
		temp = i;
		flag = false;
		while (temp!=0)
		{
			if (temp % 1000 == 666)
			{
				flag = true;
				break;
			}
			temp /= 10;
		}
		if (flag) cnt++;
		i++;
	}
	cout << i - 1;
	return 0;
}