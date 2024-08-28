#include <bits/stdc++.h>
using namespace std;

int main(){

int N; cin >> N;
for (int i = 1; i <= N; i++){
    int S = i % 3;
    if (S == 0){
        cout << "x";
    }
    else{
        cout << "o";
    }

}

    return 0;
}