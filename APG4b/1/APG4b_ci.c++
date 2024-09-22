#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  int A, B, C;
  cin >> A >> B >> C;
  vector<int> v = {A, B, C}; // 配列の初期化
  sort(v.begin(), v.end()); // ソート
  cout << v.at(2) - v.at(0) << endl;
}
