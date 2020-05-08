//#include <iostream>
//
//using namespace std;
//int main()
//{
//	unsigned int x, y, w, h;
//	cin >> x >> y >> w >> h;
//
//	if (x <= w / 2)
//	{
//		if (y <= h / 2)
//			cout << (x < y ? x : y);
//		else
//			cout << (x < h - y ? x : h - y);
//	}
//	else
//	{
//		if (y <= h / 2)
//			cout << (w - x < y ? w - x : y);
//		else
//			cout << (w - x < h - y ? w - x : h - y);
//	}
//	return 0;
//}