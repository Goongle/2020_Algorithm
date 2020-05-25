//#include <iostream>
//
//using namespace std;
//
//bool arr[14][14];
//int cnt = 0, n;
//
//bool check(int y, int x) {
//	int i, j;
//	for (i = 0; i < y; i++) {
//		if (arr[i][x] == true) 	return false;
//	}
//	for (i = y - 1, j = x - 1; i >= 0, j >= 0; i--, j--) {
//		if (arr[i][j] == true) 	return false;
//	}
//	for (i = y - 1, j = x + 1; i >= 0, j < n; i--, j++) {
//		if (arr[i][j] == true)  return false;
//	}
//	return true;
//}
//void dfs(int y) {
//	int x;
//	if (y == n) {
//		cnt++;
//	}
//	for (x = 0; x < n; x++) {
//		if (!arr[y][x] && check(y, x)) {
//			arr[y][x] = true;
//			dfs(y + 1);
//			arr[y][x] = false;
//		}
//	}
//}
//
//int main() 
//{
//	cin >> n;
//	dfs(0);
//	cout << cnt << '\n';
//	return 0;
//}