#include <bits/stdc++.h>
using namespace std;

//累積和を計算する関数
void cumulative_sum(vector<int> &S, vector<int> &A, int i, int &N) {
  if(i == N+1) {
    return;
  }
  S.at(i) = S.at(i-1) + A.at(i-1);
  cumulative_sum(S, A, i+1, N);
  return;
}

int main() {
  // ここにプログラムを追記
  int N, Q;
  cin >> N >> Q;
  vector<int> A(N);
  for(int i=0; i<N; i++) {
    cin >> A.at(i);
  } 

  //累積和を計算
  vector<int> S(N+1, 0); //Sは累積和を格納する配列
  S.at(0) = 0;
  //累積和を計算する関数を呼び出す
  cumulative_sum(S, A, 1, N);

  //クエリ処理
  for(int i=0; i<Q; i++) {
    int l, r;
    cin >> l >> r;
    cout << S.at(r) - S.at(l-1) << endl;
  }
}
