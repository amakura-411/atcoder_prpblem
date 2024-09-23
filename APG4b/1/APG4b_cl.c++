#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  int N, A, B, num;
  string op;
  cin >> N >> A;
  num = A;
  for(int i = 0; i<N; i++){
    cin >> op >> B;
    if(op == "+"){
      num += B;
    }else if(op == "-"){
      num -= B;
    }else if(op == "*"){
      num *= B;
    }else if(op == "/"){
      if(B == 0){
        cout << "error" << endl;
        break;
      }else{
        num /= B;
      }
    }
    cout << i + 1  << ":" << num << endl;
  }
}
