#include <iostream>

int Synergy[20][20], min = 10000;
bool V[20];
int n, teamS, teamL, total = 0;
int Fact(int n) {
	int res = 1;
	while (n - 1) {
		res *= n;
		n--;
	}
	return res;
}
int fin;
void DFS(int cnt) {
	if (cnt == n / 2) {
		teamS = 0;
		teamL = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (V[i] && V[j])
					teamS += Synergy[i][j] + Synergy[j][i];
				else if (!V[i] && !V[j])
					teamL += Synergy[i][j] + Synergy[j][i];
			}
		}
		min = min < abs(teamS - teamL) ? min : abs(teamS - teamL);
		total++;
		if (total == fin / 2) {
			std::cout << min << '\n';
			exit(1);
		}
		return;
	}
	for (int i = 0; i < n; i++) {
		if (!V[i]) {
			V[i] = true;
			DFS(cnt + 1);
			V[i] = false;
		}
	}
}
int main()
{
	std::cin >> n;
	fin = Fact(n) / (Fact(n / 2)*Fact(n / 2));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			std::cin >> Synergy[i][j];
		}
	}
	DFS(0);
	return 0;
}