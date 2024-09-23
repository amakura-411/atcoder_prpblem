#include <bits/stdc++.h>
using namespace std;

int count_report_num(vector<vector<int>> &children, int x) {
  // (ここに追記して再帰関数を実装する)
  // cout << "x: " << x << endl;
  if(children.at(x).size() == 0) {
    return 1;
  }
  int sum = 0;
  for(int g : children.at(x)) {
    sum += count_report_num(children, g);
  }
  // cout << "max_sum: " << max_sum + 1 << endl;
  return sum + 1;
}

int main() {
  // ここにプログラムを追記
  int N;
  cin >> N;
  vector<int> p(N);  // 各組織の親組織を示す配列
  p.at(0) = -1;  // 0番組織の親組織は存在しないので-1を入れておく
  for (int i = 1; i < N; i++) {
    cin >> p.at(i);
  }

  // 組織の関係から2次元配列を作る
  vector<vector<int>> children(N);  // ある組織の子組織の番号一覧
  for (int i = 1; i < N; i++) {
    int parent = p.at(i);  // i番の親組織の番号
    children.at(parent).push_back(i);  // parentの子組織一覧にi番を追加
  }
    // 各組織について、答えを出力
  for (int i = 0; i < N; i++) {
    cout << count_report_num(children, i) << endl;
  }
}
