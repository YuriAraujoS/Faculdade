#include <bits/stdc++.h>
using namespace std;

int main(){

int L, Y; cin >> L >> Y;
int nota = 0;
if((L-1) % 2 == 0 && (Y-1) % 2 == 0 && L != 0 && Y != 0){
    nota++;
}
if(L % 2 == 0 && Y % 2 == 0  && L != 0 && Y != 0 && L!= 4 && Y != 4  or (L == 7 && Y == 7) or (L == 3 && Y ==3)){
    nota += 2;
}
if(L >= 4 && Y >= 4){
    nota += 4;
}
cout << nota;
  return 0;
}