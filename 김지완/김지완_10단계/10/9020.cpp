//#include <iostream>
//
//using namespace std;
//int main()
//{
//	unsigned int T, n;
//	cin >> T;
//	for (unsigned int i = 0; i < T; i++)
//	{
//		cin >> n;
//		unsigned int *prime = new unsigned int[n + 1];
//		for (int i = 0; i <= n; i++)
//		{
//			prime[i] = 0;
//		}
//		for (unsigned int i = 2; i <= n; i++) {
//			if (prime[i] == false)
//			{
//				for (unsigned int j = i * 2; j <= n; j += i) {
//					prime[j] = true;
//				}
//			}
//		}
//		prime[1] = 1;
//		for (unsigned int i = 2; i <= n; i++) {
//			prime[i] = !prime[i];
//		}
//		for (unsigned int i = 0; i < n / 2; i++)
//		{
//			if (prime[n / 2 + i] && prime[n / 2 - i])
//			{
//				cout << n / 2 - i << " " << n / 2 + i << "\n";
//				break;
//			}
//		}
//		delete[] prime;
//	}
//
//	return 0;
//}