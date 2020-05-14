//#include <iostream>
//#include <string>
//#define SWAP(x,y) {string t = x; x = y; y = t;}
//
//
//using namespace std;
//void qSort(string *arr, int left, int right)
//{
//	int mLeft = left, mRight = right;
//	int pivot = arr[(left + right) / 2].length();
//
//	while (mLeft <= mRight)
//	{
//		while (arr[mLeft].length() < pivot)
//			mLeft++;
//		while (arr[mRight].length() > pivot)
//			mRight--;
//
//		if (mLeft <= mRight)
//		{
//			SWAP(arr[mLeft], arr[mRight]);
//			mLeft++, mRight--;
//		}
//	}
//	if (left < mRight) qSort(arr, left, mRight);
//	if (mLeft < right) qSort(arr, mLeft, right);
//}
//void qSort2(string *arr, int left, int right)
//{
//	int mLeft = left, mRight = right;
//	string pivot = arr[(left + right) / 2];
//
//	while (mLeft <= mRight)
//	{
//		while (arr[mLeft] < pivot)
//			mLeft++;
//		while (arr[mRight] > pivot)
//			mRight--;
//
//		if (mLeft <= mRight)
//		{
//			SWAP(arr[mLeft], arr[mRight]);
//			mLeft++, mRight--;
//		}
//	}
//	if (left < mRight) qSort2(arr, left, mRight);
//	if (mLeft < right) qSort2(arr, mLeft, right);
//}
//int main()
//{
//	int n, i, j;
//	string word;
//	string words[20000];
//	cin >> n;
//	for (i = 0; i < n; i++)
//		cin >> words[i];
//
//	qSort(words, 0, n - 1);
//	for (i = 0; i < n; i++)
//	{
//		for (j = i + 1; j < n; j++)
//		{
//			if (j == n - 1 && words[i].length() == words[j].length())
//			{
//				qSort2(words, i, j);
//				break;
//			}
//			if (words[i].length() != words[j].length())
//			{
//				qSort2(words, i, j - 1);
//				break;
//			}
//		}
//		i = j - 1;
//	}
//	for (i = 0; i < n; i++)
//	{
//		if (words[i] != words[i + 1])
//			cout << words[i] << '\n';
//	}
//	return 0;
//}