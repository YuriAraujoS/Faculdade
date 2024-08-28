#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
int c; cin >> c;
int x; cin >> x;
int ovos;
for(int i = 0; i < n;i++){
    int y; cin >> y;
    if(y < x){
        x = y;
}
ovos = c / x;
round(ovos);
}
if(ovos <= n){
cout << ovos;}
else{
    cout << n;
}
  return 0;
}