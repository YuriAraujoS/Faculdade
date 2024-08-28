#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
for(int i = 0; i < n; i++){
    int x, y, z; cin >> x >> y >> z;
    if(x == y){
        cout << z << '\n';
    }
    else if(x == z){
        cout << y << '\n';
    }
    else{
    cout << x << '\n';
    }
}

  return 0;
}