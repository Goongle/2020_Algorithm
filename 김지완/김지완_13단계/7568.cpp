//#include <iostream>
//using namespace std;
//
//int main()
//{
//	int N, x, y, temp;
//	cin >> N;
//	int *arr = new int[N];
//	int *arr2 = new int[N];
//	int *arr3 = new int[N];
//	int *ans = new int[N];
//	for (int i = 0; i < N; i++)
//	{
//		cin >> x >> y;
//		arr[i] = x;
//		arr2[i] = y;
//		arr3[i] = i;
//	}
//	for (int i = 0; i < N; i++)
//	{
//		for (int j = 0; j < N - i - 1; j++)
//		{
//			if (arr[j] > arr[j + 1])
//			{
//				temp = arr[j + 1];
//				arr[j + 1] = arr[j];
//				arr[j] = temp;
//				temp = arr2[j + 1];
//				arr2[j + 1] = arr2[j];
//				arr2[j] = temp;
//				temp = arr3[j + 1];
//				arr3[j + 1] = arr3[j];
//				arr3[j] = temp;
//			}
//		}
//	}
//
//	for (int i = 0; i < N; i++)
//	{
//		int cnt = 1;
//		for (int j = i + 1; j < N; j++)
//		{
//			if (arr[i] < arr[j] && arr2[i] < arr2[j])
//			{
//				cnt++;
//			}
//		}
//		ans[arr3[i]] = cnt;
//	}
//	for (int i = 0; i < N; i++)
//	{
//		cout << ans[i] << ' ';
//	}
//	return 0;
//}