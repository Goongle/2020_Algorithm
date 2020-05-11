//#include <iostream>
//
//using namespace std;
//int main()
//{
//	unsigned int x, y, z;
//	while (1)
//	{
//		cin >> x >> y >> z;
//		if (x == 0 && y == 0 && z == 0)
//			break;
//		if (x >= y)
//		{
//			if (x >= z)
//			{
//				if (x*x == y*y + z*z)
//					cout << "right" << "\n";
//				else
//					cout << "wrong" << "\n";
//			}
//			else
//			{
//				if (z*z == y*y + x*x)
//					cout << "right" << "\n";
//				else
//					cout << "wrong" << "\n";
//			}
//		}
//		else
//		{
//			if (y >= z)
//			{
//				if (y*y == x*x + z*z)
//					cout << "right" << "\n";
//				else
//					cout << "wrong" << "\n";
//			}
//			else
//			{
//				if (z*z == y*y + x*x)
//					cout << "right" << "\n";
//				else
//					cout << "wrong" << "\n";
//			}
//		}
//	}
//	return 0;
//}