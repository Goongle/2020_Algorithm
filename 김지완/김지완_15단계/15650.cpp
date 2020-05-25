//#include <iostream>
//
//using namespace std;
//
//int arr[9];
//int m, n;
//void dfs(int cnt, int start)
//{
//	if (cnt == m)
//	{
//		for (int i = 0; i < m; i++)
//			cout << arr[i] << ' ';
//		cout << '\n';
//		return;
//	}
//	for (int i = start; i <= n; i++)
//	{
//		arr[cnt] = i;
//		dfs(cnt + 1, i + 1);
//	}
//}
//int main()
//{
//	cin >> n >> m;
//	dfs(0, 1);
//
//	return 0;
//}