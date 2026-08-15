#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  int a;
  int b;
  cin >> a >> b;

  bool nineFlag = false;
  if (a + b == 9) {
    nineFlag = true;
  }
  if (a - b == 9) {
    nineFlag = true;
  }
  if (a * b == 9) {
    nineFlag = true;
  }
  if (a / b == 9) {
    nineFlag = true;
  }

  if (nineFlag) {
    cout << "Nine" << endl;
  } else {
    cout << "Nein" << endl;
  }
}
