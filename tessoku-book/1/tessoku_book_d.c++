#include <bits/stdc++.h>
using namespace std;

void binary_representation(int n, int k) {
  if(k == 0) {
    cout << n << endl;
    return;
  }
  int wari = (1 << k);
  cout << n / wari;
  binary_representation(n % wari, k - 1);
  return;
}


int main() {
  // ここにプログラムを追記
  int N;
  int keta = 9;
  cin >> N;
  binary_representation(N, keta); 
}
