//#include <iostream>
//
//using namespace std;
//int main()
//{
//	int N;
//	cin >> N;
//
//	int temp = N;
//	int sum;
//	int cnt = 1;
//
//	while (temp / 10 != 0)
//	{
//		temp /= 10;
//		cnt++;
//	}
//
//	if (cnt == 1)
//	{
//		if (N % 2 == 0)
//			cout << N / 2 << '\n';
//		else
//			cout << 0 << '\n';
//	}
//	else
//	{
//		for (int i = N - cnt * 9; i < N; i++)
//		{
//			temp = i;
//			sum = i;
//			while (temp / 10 != 0)
//			{
//				sum += temp % 10;
//				temp /= 10;
//			}
//			sum += temp;
//			if (sum == N)
//			{
//				cout << i << '\n';
//				break;
//			}
//			if (i == N - 1)
//			{
//				cout << 0 << '\n';
//				break;
//			}
//		}
//	}
//	
//	return 0;
//}