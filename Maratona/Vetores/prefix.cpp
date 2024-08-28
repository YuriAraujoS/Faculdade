#include <bits/stdc++.h>
using namespace std;

int main(){

    int n; cin >> n;
    for (int i = 0; i < n; i++){
        int len; cin >> len;
        int x; cin >> x;
        vector <int> digits(0);
        for (int j = 0; j < len; j++){
            for(int k = 0; k < 10; k++){
                if ((x - (k * int(pow(10, j)))) % int(pow(10, j + 1)) == 0){
                    x -= k * int(pow(10, j));
                    digits.push_back(k);
                    break;
                }
            }
        }
        sort(digits.begin(), digits.end());
        int moves = 0;
        for (int d = 0; d < len - 1; d++){
            if(digits[d] == digits[d + 1]){
                moves++;
            }
        }
        cout << moves << '\n';
    }

  return 0;
}