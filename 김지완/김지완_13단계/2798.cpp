//#include <iostream>
//using namespace std;
//
//int main()
//{
//	int M, N, n;
//	cin >> N >> M;
//	int *arr = new int[N];
//
//	for (int i = 0; i < N; i++)
//	{
//		cin >> n;
//		arr[i] = n;
//	}
//
//	int sum = 0;
//	for (int i = 0; i < N - 2; i++)
//	{
//		for (int j = i + 1; j < N - 1; j++)
//		{
//			for (int k = j + 1; k < N; k++)
//			{
//				int m = arr[i] + arr[j] + arr[k];
//				if (sum < m && m <= M)
//				{
//					sum = m;
//				}
//			}
//		}
//	}
//	cout << sum << '\n';
//	return 0;
//}