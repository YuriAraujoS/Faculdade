#include <bits/stdc++.h>
using namespace std;

int main(){
int N, K; cin >> N >> K;
for (int i = 0; i < N; i++){
    int A; cin >> A;
    int D = A % K;
    if (D == 0){
        cout << A / K << " ";
    }
}
cout << '\n';
    return 0;
}