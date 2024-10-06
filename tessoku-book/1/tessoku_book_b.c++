#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  int N, X, A;
  cin >> N >> X;
  bool flag = false;
  for(int i=0; i<N; i++){
    cin >> A;
    if(A == X) {
      flag = true;
    }
  }
  if(flag) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
