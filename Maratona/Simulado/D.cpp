#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
for(int i = 0; i < n; i++){
    int x; cin >> x;
    int palitos = 0;
        for(int p = 0; p < x; p++){
            int y; cin >> y;
            palitos += y;
        }
    long long palitosqrt = sqrt(palitos);
    if(palitosqrt == round(sqrt(palitos))){
        cout << "YES" << '\n';
    }
    else{
        cout << "NO" << '\n';
    }
}

  return 0;
}