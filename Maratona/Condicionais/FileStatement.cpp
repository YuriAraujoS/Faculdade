#include <bits/stdc++.h>
using namespace std;

int main(){

int N; cin >> N;
int AC, WA, TLE, RE; AC = 0; WA = 0; TLE = 0; RE = 0;
for (int i = 0; i < N; i++){
    string k; cin >> k;
    if (k == "AC") AC++;
    if (k == "WA") WA++;
    if (k == "TLE") TLE++;
    if (k == "RE") RE++;
}
cout << "AC x " << AC << '\n';
cout << "WA x " << WA << '\n';
cout << "TLE x " << TLE << '\n';
cout << "RE x " << RE << '\n';
return 0;
}