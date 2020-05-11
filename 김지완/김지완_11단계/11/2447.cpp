//#include <iostream>
//
//using namespace std;
//void star(int n, int start1, int start2, char **arr)
//{
//	if (n == 3)
//	{
//		for (int i = start1; i < start1 + n; i++)
//		{
//			for (int j = start2; j < start2 + n; j++)
//			{
//				if (i == start1 + 1 && j == start2 + 1)
//					arr[i][j] = ' ';
//				else
//					arr[i][j] = '*';
//			}
//		}
//	}
//	else
//	{
//		int a = start1 + n / 3;
//		int b = start1 + 2 * n / 3;
//		int c = start2 + n / 3;
//		int d = start2 + 2 * n / 3;
//		for (int i = start1; i < start1 + n; i++)
//		{
//			for (int j = start2; j < start2 + n; j++)
//			{
//				if (a <= i && i < b && c <= j && j < d)
//					arr[i][j] = ' ';
//				else if (i % (n / 3) == 0 && j % (n / 3) == 0)
//				{
//					star(n / 3, i, j, arr);
//				}
//			}
//		}
//	}
//}
//void print(int n, char **arr)
//{
//	for (int i = 0; i < n; i++)
//	{
//		for (int j = 0; j < n; j++)
//		{
//			cout << arr[i][j];
//		}
//		cout << '\n';
//	}
//}
//int main()
//{
//	int N;
//	cin >> N;
//	char **arr = new char*[N];
//	for (int i = 0; i < N; i++)
//		arr[i] = new char[N];
//	star(N, 0, 0, arr);
//	print(N, arr);
//
//	delete[] arr;
//	return 0;
//}