//#include <iostream>
//
//using namespace std;
//int main()
//{
//	int n, num, temp;
//	cin >> n;
//	int *arr = new int[n];
//	for (int i = 0; i < n; i++)
//	{
//		cin >> num;
//		arr[i] = num;
//	}
//	for (int i = 0; i < n; i++)
//	{
//		for (int j = 0; j < n - i - 1; j++)
//		{
//			if (arr[j] > arr[j + 1])
//			{
//				temp = arr[j + 1];
//				arr[j + 1] = arr[j];
//				arr[j] = temp;
//			}
//		}
//	}
//	for (int i = 0; i < n; i++)
//	{
//		cout << arr[i] << '\n';
//	}
//	return 0;
//}