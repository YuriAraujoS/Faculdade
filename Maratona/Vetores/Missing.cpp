#include <bits/stdc++.h>
using namespace std;

int main(){
int n; cin >> n;
int z = 0;
 int m = 0;
vector<int> N(0);
for(int i = 1; i < n; i++){
    int x; cin >> x;
    z += (i+1);
    m += x;
}
cout << z + 1 - m;
    return 0;
}