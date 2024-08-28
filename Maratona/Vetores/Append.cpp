#include <bits/stdc++.h>
using namespace std;

int main(){

int Q; cin >> Q;
vector<int> A(0);
for(int i = 0; i < Q; i++){
string y; cin >> y;
    if (y == "1"){
        int x; cin >> x;
        A.push_back(x);
    }
    else if (y == "2") {
        int x; cin >> x;
        if (x < A.size()){
            cout << A[x] << '\n';}
        else {
            cout << A[A.size() - x] << '\n';}
}
}
return 0;
}