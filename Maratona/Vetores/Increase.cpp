#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
vector<int> A(0);
long long moves = 0;
int y; cin >> y;
A.push_back(y);
for (int i = 1; i < n; i++){
    int x; cin >> x;
    A.push_back(x);
    while (A[i] < A[i-1]){
        A[i]++;
        moves++;
    }
}
cout << moves;
  return 0;
}