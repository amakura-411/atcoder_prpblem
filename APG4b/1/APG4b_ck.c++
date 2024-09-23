#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  // 1+1+1-1 ->偶数の場合数値、奇数の場合文字列
  string s;
  cin >> s;
  int num = 1;
  for (int i=1; i<s.size(); i+=2){
    if (s.at(i) == '+'){
      num++;
    }else if (s.at(i) == '-'){
      num--;
    }
  }
  cout << num << endl;
}
