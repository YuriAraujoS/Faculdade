#include <bits/stdc++.h>
using namespace std;

int main(){

    int t; cin >> t;
    for (int i = 0; i < t; i++){
        int n; cin >> n;
        vector <int> A(0);
        for (int j = 0; j < n; j++){
            int a; cin >> a;
            A.push_back(a);
        }
        sort(A.begin(), A.end());
        int point = 0;
        for (int k = 0; k < n - 1; k++){
            if (A[k] == A[k + 1]){
                point += 1;
            }
        }
        cout << point << '\n';
    }
    return 0;
}