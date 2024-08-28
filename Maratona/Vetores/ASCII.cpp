#include <bits/stdc++.h>
using namespace std;

int main(){

int H, W; cin >> H >> W;
char z;
vector<vector<char>> A({0, vector<char>{0}});
for(int p = 0; p < H; p++){
    vector<char> C(0);
for (int i = 0; i < W; i++){
    int x; cin >> x;
    if (x == 0){
        z = '.';
    }
    else{
        z = 'A' + (x-1);
    }
    C.push_back(z);
    cout << C[i];
}
cout << '\n';
}
  return 0;
}