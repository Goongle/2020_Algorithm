//#include <iostream>
//
//using namespace std;
//int main()
//{
//	int N, M;
//	int min= 10000;
//	char color;
//	cin >> N >> M;
//	char **arr = new char*[N];
//	for (int i = 0; i < N; i++)
//		arr[i] = new char[M];
//	char W[8][8];
//	char B[8][8];
//	for (int i = 0; i < 8; i++)
//	{
//		for (int j = 0; j < 8; j++)
//		{
//			if ((i % 2 == 0 && j % 2 == 0)||(i % 2 == 1 && j % 2 == 1))
//			{
//				B[i][j] = 'B';
//				W[i][j] = 'W';
//			}
//			else
//			{
//				B[i][j] = 'W';
//				W[i][j] = 'B';
//			}
//		}
//	}
//	for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < M; j++)
//		{
//			cin >> color;
//			arr[i][j] = color;
//		}
//	}
//	for (int k = 0; k < N - 7; k++)
//	{
//		for (int l = 0; l < M - 7; l++)
//		{
//			int min2;
//			int cntB = 0;
//			int cntW = 0;
//			for (int i = k; i < k + 8; i++)
//			{
//				for (int j = l; j < l + 8; j++)
//				{
//					if (arr[i][j] != B[i - k][j - l])
//						cntB++;
//					else if (arr[i][j] != W[i - k][j - l])
//						cntW++;
//				}
//			}
//			min2 = cntB < cntW ? cntB : cntW;
//			min = min < min2 ? min : min2;
//		}
//	}
//	cout << min;
//	return 0;
//}