//#include <iostream>
//
//#define qSWAP(x, y) { int t = x; x = y; y = t; }
//using namespace std;
//int arr[10];
//
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
//
//int main()
//{
//	int n, i = 0;
//	cin >> n;
//	while (n / 10)
//	{
//		arr[i] = n % 10;
//		n /= 10;
//		i++;
//	}
//	arr[i] = n;
//	i++;
//	qSort(arr, 0, i - 1);
//	for (int j = i - 1; j >= 0; j--)
//	{
//		cout << arr[j];
//	}
//	
//	return 0;
//}