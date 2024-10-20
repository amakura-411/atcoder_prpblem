#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<vector<int>> S;
  int H, W, Q;
  cin >> H >> W;

  for(int i =0; i<H; i++) {
    vector<int> A;
    for(int j=0; j<W; j++) {
      int a;
      cin >> a;
      A.push_back(a);
    }
    S.push_back(A);
  }

  //累積和を計算
  vector<vector<int>> T(H+1, vector<int>(W+1, 0));
  for(int i=1; i<=H; i++) {
    for(int j=1; j<=W; j++) {
      T[i][j] = T[i-1][j] + T[i][j-1] - T[i-1][j-1] + S[i-1][j-1];
    }
  }

  //クエリ処理
  cin >> Q;
  for(int i=0; i<Q; i++) {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    cout << T[x2][y2] - T[x1-1][y2] - T[x2][y1-1] + T[x1-1][y1-1] << endl;
  }


}

