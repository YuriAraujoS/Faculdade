#include <bits/stdc++.h>
using namespace std;

int main(){
int n; cin >> n;
string alfabeto = "abcdefghijklmnopqrstuvwxyz";
vector<int> ver(0);
for(int i = 0; i < 26; i++){
  ver.push_back(-1);
}
for(int i = 0; i < n; i++){
    int x; cin >> x;
    string k, bi; cin >> k; 
    bi = "";
    bool a = 1;
    for(int j = 0; j < x; j++){
      if (j == 0){
        bi += 1;
      }
      
      
    }
    if (a == 1){
      cout << "YES" << '\n';
    }
    else{
      cout << "NO" << '\n';
    }
}

  return 0;
}