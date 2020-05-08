#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	unsigned int x1, y1, r1, x2, y2, r2, T;
	cin >> T;
	for (unsigned int i = 0; i < T; i++)
	{
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		double d = sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
		if (r1 < r2)
		{
			unsigned int temp;
			temp = r1;
			r1 = r2;
			r2 = temp;
		}
		if (x1 == x2 &&y1 == y2 &&r1 == r2)
			cout << -1 << "\n";
		else if (r1 + r2 < d)
			cout << 0 << "\n";
		else if (r1 + r2 == d)
			cout << 1 << "\n";
		else
		{
			if (d + r2 < r1)
				cout << 0 << "\n";
			else if (d + r2 == r1)
				cout << 1 << "\n";
			else
				cout << 2 << "\n";
		}
	}
	return 0;
}