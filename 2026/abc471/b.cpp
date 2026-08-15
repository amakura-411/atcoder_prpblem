#include <bits/stdc++.h>

#include <algorithm>
#include <iostream>
#include <string>
using std::tolower;

using namespace std;

int main() {
  // ここにプログラムを追記
  int n;
  cin >> n;

  map<string, int> words;

  int maxNum = 1;
  for (int i = 0; i < n; i++) {
    string str;
    cin >> str;
    for (char& s : str) {
      s = tolower(s);
    }
    if (words.count(str) == 1) {
      words[str] += 1;
      maxNum = max(maxNum, words[str]);
    } else {
      words[str] = 1;
    }
  }
  cout << maxNum << '\n';
}
