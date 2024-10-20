#include <bits/stdc++.h>
using namespace std;

int main() {
  int D, N;
  //D日間、N人の人
  cin >> D >> N;

 // 配列11
  int L, R;
  vector<int> T(D + 2, 0);
  for (int i=0; i<N; i++) {
    cin >> L >> R;
    // cout << L << " "<< R << endl;
    T[L]++;
    T[R+1]--;
    // cout << T[L] << " " << T[R+1] << endl;
  }

  // 累積和を計算
  vector<int> S(D+1, 0);
  S[0] = 0;
  for(int i=1; i<=D; i++) {
    S[i] = S[i-1] + T[i];
    // cout << S[i-1] << T[i] << endl;
  }


  for(int   i=1; i<=D; i++) {
    // cout << i << "番目：" << endl;
    cout << S[i] << endl;
  }

}