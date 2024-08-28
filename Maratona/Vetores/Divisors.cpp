#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
int d;
for (int i = 0; i < n; i++){
d = 0;
int x; cin >> x;
    for (int p = 1; p <= sqrt(x); p++){
        if(x % p == 0){
            d += 2;
        }
    }
if (sqrt(x) == round(sqrt(x))){
    d--;
}
cout << d << '\n';
}
  return 0;
}