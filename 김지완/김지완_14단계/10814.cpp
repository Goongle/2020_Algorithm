#include <iostream>
#include <string>
#define SWAP(x,y,type) do{type t; t = x; x = y; y = t;}while(0)

using namespace std;
int ages[100000];
int orders[100000];
string names[100000];
void qSort(int *ages, int *orders, string * names, int left, int right)
{
	int mLeft = left, mRight = right;
	int pivot = ages[(left + right) / 2];

	while (mLeft <= mRight)
	{
		while (ages[mLeft] < pivot)
			mLeft++;
		while (ages[mRight] > pivot)
			mRight--;

		if (mLeft <= mRight)
		{
			SWAP(ages[mLeft], ages[mRight], int);
			SWAP(orders[mLeft], orders[mRight], int);
			SWAP(names[mLeft], names[mRight], string);
			mLeft++, mRight--;
		}
	}

	if (left < mRight) qSort(ages, orders, names, left, mRight);
	if (mLeft < right) qSort(ages, orders, names, mLeft, right);
}
int main()
{
	int n, i, j;
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> ages[i] >> names[i];
		orders[i] = i;
	}
	qSort(ages, orders, names, 0, n - 1);
	for (i = 0; i < n; i++)
	{
		for (j = i + 1; j < n; j++)
		{
			if (j == n - 1 && ages[i] == ages[j])
			{
				qSort(orders, ages, names, i, j);
				break;
			}
			if (ages[i] != ages[j])
			{
				qSort(orders, ages, names, i, j - 1);
				break;
			}
		}
		i = j - 1;
	}
	for (i = 0; i < n; i++)
		cout << ages[i] << ' ' << names[i] << '\n';

	return 0;
}