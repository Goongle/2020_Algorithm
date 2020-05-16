//#include <iostream>
//#define SWAP(x, y) {int t = x; x = y; y = t;}
//
//int X[100000];
//int Y[100000];
//void quickSort(int *arr, int *arr2, int Left, int Right)
//{
//	int mLeft = Left;
//	int mRight = Right;
//	int pivot = arr[(Left + Right) / 2];
//	while (mLeft <= mRight)
//	{
//		while (pivot > arr[mLeft])	mLeft++;
//		while (pivot < arr[mRight])	mRight--;
//
//		if (mLeft <= mRight)
//		{
//			SWAP(arr[mLeft], arr[mRight]);
//			SWAP(arr2[mLeft], arr2[mRight]);
//			mLeft++, mRight--;
//		}
//	}
//	if (Left < mRight) quickSort(arr, arr2, Left, mRight);
//	if (mLeft < Right) quickSort(arr, arr2, mLeft, Right);
//}
//
//using namespace std;
//int main()
//{
//	int n, i, j;
//	cin >> n;
//	for (i = 0; i < n; i++)
//	{
//		cin >> X[i] >> Y[i];
//	}
//
//	quickSort(Y, X, 0, n - 1);
//	
//	for (i = 0; i < n; i++)
//	{
//		for (j = i + 1; j < n; j++)
//		{
//			if (j == n - 1 && Y[i] == Y[j])
//			{
//				quickSort(X, Y, i, j);
//				break;
//			}
//			if (Y[i] != Y[j])
//			{
//				quickSort(X, Y, i, j - 1);
//				break;
//			}
//		}
//		i = j - 1;
//	}
//
//	for (i = 0; i < n; i++)
//	{
//		cout << X[i] << ' ' << Y[i] << '\n';
//	}
//	return 0;
//}