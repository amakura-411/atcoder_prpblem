#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }

  // dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
  // ここにプログラムを追記
  bool flag = false;
  // 1.ループを使わないで書く
  // if(data.at(0) == data.at(1)) flag = true;
  // if(data.at(1) == data.at(2)) flag = true;
  // if(data.at(2) == data.at(3)) flag = true;
  // if(data.at(3) == data.at(4)) flag = true;

  // 2.ループを使って書く
  for(int i = 0; i < 4; i++){
    if(data.at(i) == data.at(i + 1)){
      flag = true;
    }
  }

  if(flag){
    cout << "YES" << endl;
  }else{
    cout << "NO" << endl;
  }

}
