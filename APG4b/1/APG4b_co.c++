#include <bits/stdc++.h>
using namespace std;

int main() {
  int p;
  cin >> p;
  if (p == 2) {
    // 1行目で、たこ焼きセットの説明文 textの末尾に!をつけて出力します。
    string text;
    cin >> text;
    cout << text << "!" << endl;
  }
  int price, N;
  cin >> price >> N;
  cout << price * N << endl;
}
