//#include <iostream>
//
//using namespace std;
//
//int main()
//{
//	unsigned int N, M;
//	cin >> M >> N;
//
//	unsigned int prime[1000000] = { 0, };
//
//	for (unsigned int i = 2; i <= N; i++) {
//		for (unsigned int j = i * 2; j <= N; j += i) {
//			prime[j] = true;
//		}
//	}
//
//	for (unsigned int i = 2; i <= N; i++) {
//		prime[i] = !prime[i];
//	}
//	for (unsigned int i = M; i <= N; i++) {
//		if (prime[i] == true)cout << i << "\n";
//	}
//	return 0;
//}