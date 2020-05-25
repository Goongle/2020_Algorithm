//#include <iostream>
//
//using namespace std;
//int sudoku[9][9];
//bool row[9][10];
//bool col[10][9];
//bool square[9][9];
//void print() {
//	for (int i = 0; i < 9; i++) {
//		for (int j = 0; j < 9; j++) {
//			cout << sudoku[i][j] << ' ';
//		}
//		cout << '\n';
//	}
//}
//void dfs(int n) {
//	int y = n / 9;
//	int x = n % 9;
//	if (n == 81) {
//		print();
//		exit(0);
//	}
//	if (sudoku[y][x] == 0) {
//		for (int i = 0; i < 9; i++) {
//			if (!row[y][i + 1] && !col[i + 1][x] && !square[(y / 3) * 3 + i / 3][(x / 3) * 3 + i % 3]) {
//				row[y][i + 1] = true;
//				col[i + 1][x] = true;
//				square[(y / 3) * 3 + i / 3][(x / 3) * 3 + i % 3] = true;
//				sudoku[y][x] = i + 1;
//				dfs(n + 1);
//				row[y][i + 1] = false;
//				col[i + 1][x] = false;
//				square[(y / 3) * 3 + i / 3][(x / 3) * 3 + i % 3] = false;
//				sudoku[y][x] = 0;
//			}
//		}
//	}
//	else
//		dfs(n + 1);
//}
//int main()
//{
//	for (int i = 0; i < 9; i++) {
//		for (int j = 0; j < 9; j++) {
//			cin >> sudoku[i][j];
//			if (sudoku[i][j]) {
//				row[i][sudoku[i][j]] = true;
//				col[sudoku[i][j]][j] = true;
//				square[(i / 3) * 3 + (sudoku[i][j] - 1) / 3][(j / 3) * 3 + (sudoku[i][j] - 1) % 3] = true;
//			}
//		}
//	}
//	dfs(0);
//	return 0;
//}