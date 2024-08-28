#include <bits/stdc++.h>
using namespace std;

int main(){

//número de casos e repetição para cada um deles
int t; cin >> t;
for (int i = 0; i < t; i++){
    //inserindo o número de digitos e o dígito que queremos inserir
    int n; cin >> n; char k; cin >> k;
    //inserindo uma string de dígitos e uma string vazia para alterarmos dps
    string p; cin >> p; p = p + "0";
    string g = "";
    //setando um valor booleano para cancelar depois quando o dígito por inserido
    bool v = 1;
    //verificação para cada dígito para inserirmos o k
    for (int u = 0; u < n; u++){
        //if com o limitador
        if (v == 1){
            if (k <= p[u]){
                g += p[u];
                if (u == n - 1) {g += k;}
                }
            else{
                g += k;
                v = 0;
                u--;
            }
        }
        //continuação sem o limitador
        else{g += p[u];}
}
//string g de saída com o dígito inserido
cout << g << '\n';
}
    return 0;
}