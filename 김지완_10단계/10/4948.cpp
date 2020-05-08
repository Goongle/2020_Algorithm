//#include <iostream>
//
//using namespace std;
//int main()
//{
//	int n;
//	
//	while (1)
//	{
//		cin >> n;
//		if (n == 0)
//			break;
//		unsigned int cnt = 0;
//		unsigned int *prime = new unsigned int[2 * n + 1];
//		for (int i = 0; i <= 2 * n; i++)
//		{
//			prime[i] = 0;
//		}
//		for (unsigned int i = 2; i <= 2 * n; i++) {
//			if (prime[i] == false)
//			{
//				for (unsigned int j = i * 2; j <= 2 * n; j += i) {
//					prime[j] = true;
//				}
//			}
//		}
//		prime[1] = 1;
//		for (unsigned int i = n + 1; i <= 2 * n; i++) {
//			prime[i] = !prime[i];
//			if (prime[i])
//				cnt++;
//		}
//		cout << cnt << "\n";
//		delete[] prime;
//	}
//	return 0;
//}