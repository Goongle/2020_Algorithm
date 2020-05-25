//#include <iostream>
//
//int n, max = -1000000001, min = 1000000001, sum;
//int op[4];
//int calc[199];
//int Fact(int n) {
//	int res = 1;
//	while (n - 1) {
//		res *= n;
//		n--;
//	}
//	return res;
//}
//void Res() {
//	int v;
//	sum = calc[0];
//	for (int i = 0; i < n - 1; i++) {
//		v = calc[2 * i + 1];
//		switch (v) {
//		case 1:
//			sum += calc[2 * i + 2];
//			break;
//		case 2:
//			sum -= calc[2 * i + 2];
//			break;
//		case 3:
//			sum *= calc[2 * i + 2];
//			break;
//		case 4:
//			sum /= calc[2 * i + 2];
//			break;
//		}
//	}
//}
//void DFS(int cnt) {
//	if (cnt == n) {
//		Res();
//		max = max < sum ? sum : max;
//		min = min < sum ? min : sum;
//		return;
//	}
//	for (int i = 0; i < n - 1; i++) {
//		if (!calc[i * 2 + 1]) {
//			if (op[0]) {
//				calc[i * 2 + 1] = 1;
//				op[0]--;
//				DFS(cnt + 1);
//				op[0]++;
//			}
//			else if (op[1]) {
//				calc[i * 2 + 1] = 2;
//				op[1]--;
//				DFS(cnt + 1);
//				op[1]++;
//			}
//			else if (op[2]) {
//				calc[i * 2 + 1] = 3;
//				op[2]--;
//				DFS(cnt + 1);
//				op[2]++;
//			}
//			else if (op[3]) {
//				calc[i * 2 + 1] = 4;
//				op[3]--;
//				DFS(cnt + 1);
//				op[3]++;
//			}
//			calc[i * 2 + 1] = 0;
//		}
//	}
//}
//
//int main()
//{
//	std::cin >> n;
//	for (int i = 0; i < n; i++) {
//		std::cin >> calc[i * 2];
//	}
//	for (int i = 0; i < 4; i++) {
//		std::cin >> op[i];
//	}
//	DFS(1);
//	std::cout << max << '\n' << min << '\n';
//	return 0;
//}