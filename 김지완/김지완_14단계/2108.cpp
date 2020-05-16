//#include <iostream>
//#define qSWAP(x, y) { int t = x; x = y; y = t; }
//int arr[500000] = { 0, };
//int arr2[8001] = { 0, };
//
//using namespace std;
//void qSort(int *array, int left, int right) {
//	int mLeft = left, mRight = right;
//	int pivot = array[(left + right) / 2];
//
//	while (mLeft <= mRight) {
//		while (pivot > array[mLeft]) mLeft++;
//		while (pivot < array[mRight]) mRight--;
//
//		if (mLeft <= mRight) {
//			qSWAP(array[mLeft], array[mRight]);
//			mLeft++, mRight--;
//		}
//	}
//
//	if (left < mRight) qSort(arr, left, mRight);
//	if (mLeft < right) qSort(arr, mLeft, right);
//}
//int main()
//{
//	int n, i, max = -4001, min = 4001;
//	double sum = 0;
//	cin >> n;
//	for (i = 0; i < n; i++)
//	{
//		cin >> arr[i];
//		sum += arr[i];
//		if (max < arr[i])
//			max = arr[i];
//		if (min > arr[i])
//			min = arr[i];
//		arr2[4000 + arr[i]]++;
//	}
//	cout << round(sum / n) << '\n';
//	qSort(arr, 0, n - 1);
//	cout << arr[n / 2] << '\n';
//
//
//	int first = -1, ans;
//	bool second = false;
//	for (i = 0; i < 8001; i++)
//	{
//		if (arr2[i] > first)
//		{
//			first = arr2[i];
//			ans = i;
//			second = false;
//		}
//		else if (arr2[i] == first)
//		{
//			if (!second)
//			{
//				second = true;
//				first = arr2[i];
//				ans = i;
//			}
//		}
//	}
//	cout << ans - 4000 << '\n';
//
//
//	cout << max - min << '\n';
//
//	return 0;
//}