#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  int N, M; //参加者数: N, ゲーム数: M
  cin >> N >> M;
  vector<vector<char>> result(N, vector<char>(N, '-'));
  // resultの表示
  int a, b;
  for(int i=0; i<M; i++) {
    cin >> a >> b;
    //勝者を記録
    result.at(a-1).at(b-1) = 'o';
    //敗者を記録
    result.at(b-1).at(a-1) = 'x';
  }


  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++){
      cout << result.at(i).at(j);
      if(j != N-1) {
        cout << " ";
      }
    }
    cout << endl;
  }

}
