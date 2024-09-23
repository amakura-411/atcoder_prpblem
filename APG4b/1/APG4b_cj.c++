#include <bits/stdc++.h>
using namespace std;

int main() {
  // ここにプログラムを追記
  int N, A, points, average, num;
  points = 0;
  cin >> N;
  vector<int> point(N + 1);
  for(int i = 0; i < N; i++){
    cin >> point.at(i);
    points += point.at(i);
  }
  average = points / N;
  for(int i = 0; i < N; i++){
    num = point.at(i) - average;
    if(num < 0){
      cout << num * -1 << endl;
    }else {
      cout << num << endl;
    }
  }
}
