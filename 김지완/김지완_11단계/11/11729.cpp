#include <iostream>
using namespace std;

void hanoi(int n ,int start, int end)
{
	if (n == 1) {
		cout << start << ' ' << end << '\n';
	}
	else
	{
		hanoi(n - 1, start, 6 - (start + end));
		cout << start << ' ' << end << '\n';
		hanoi(n - 1, 6 - (start + end), end);
	}
}
int count(int N)
{
	if (N == 1)
		return 1;
	else
		return count(N - 1) * 2 + 1;
}
int main()
{
	int N;
	cin >> N;
	cout << count(N) << '\n';
	hanoi(N, 1, 3);

	return 0;
}