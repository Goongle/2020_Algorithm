//#include <iostream>
//
//using namespace std;
//bool isPrime(unsigned int n)
//{
//	if (n == 1)
//		return false;
//	for (unsigned int i = 2; i < n; i++)
//	{
//		if (n % i == 0)
//			return false;
//	}
//	return true;
//}
//int main()
//{
//	unsigned int N, M, sum = 0, min = 1000000000;
//	cin >> M >> N;
//	for (unsigned int i = M; i <= N; i++)
//	{
//		if (isPrime(i))
//		{
//			sum += i;
//			if (min > i)
//				min = i;
//		}
//	}
//	if (sum == 0)
//		cout << -1;
//	else
//		cout << sum << endl << min << endl;
//
//	return 0;
//}