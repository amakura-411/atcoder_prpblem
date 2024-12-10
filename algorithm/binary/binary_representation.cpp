#include <bits/stdc++.h>
using namespace std;

//二進数の表示(桁数指定)
void formatBinary(int n, int k) {
  if(k == 0) {
    cout << n << endl;
    return;
  }
  int wari = (1 << k);
  cout << n / wari;
  formatBinary(n % wari, k - 1);
  return;
}

//二進数の表示(再帰)
void binary_representation(int n) {
  if(n == 0) {
    return;
  }
  binary_representation(n / 2);
  cout << n % 2;
  return;
}

int main() {
  // ここにプログラムを追記
  int N;
  int keta = 9;
  cin >> N;
  formatBinary(N, keta); 
  binary_representation(N);
}
