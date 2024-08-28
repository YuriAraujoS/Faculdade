#include <bits/stdc++.h>
using namespace std;

int main(){

string x = "codeforces";
int y; cin >> y;
for (int i = 0; i < y; i++){
    string z; cin >> z;
    int n = 0;
    for (int p = 0; p < 10; p++){
        if (x[p] != z[p]){
            n++;
        }
    }
    cout << n << " ";
}
    return 0;
}