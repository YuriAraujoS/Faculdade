#include <bits/stdc++.h>
using namespace std;

int main(){

int n; cin >> n;
int p = 0;
vector<int> A(0);
for (int i = 0; i < n; i++){
int x; cin >> x;
A.push_back(x);
}
sort(A.begin(), A.end());
for (int i = 0; i < n; i++){
if (A[i] != A[i-1]){
    p++;
}
}
cout << p;
   return 0;
}