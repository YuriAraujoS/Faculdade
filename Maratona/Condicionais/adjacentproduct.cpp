#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
int x; cin >> x;
for (int i = 1; i < n; i++ ){
    int y; cin >> y;
    int p; p = x * y;
    cout << p << " ";
    x = y;
    }
cout << '\n';
    return 0;
}