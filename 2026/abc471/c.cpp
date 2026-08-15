#include <bits/stdc++.h>

#include <cmath>

using namespace std;
int main() {
  // ここにプログラムを追記
  int n;
  set<int> m;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;
    m.insert(num);
  }

  int current = 0;
  long ans = 0;
  for (int i = 0; i < n; i++) {
    auto index = m.lower_bound(current);
    int p;
    if (index == m.begin()) {
      p = *index;
    } else if (index == m.end()) {
      p = *--index;
    } else {
      int e_p = *index;
      int b_p = *--index;
      int b_abs = abs(b_p - current);
      int e_abs = abs(e_p - current);
      if (b_abs <= e_abs) {
        p = b_p;
      } else {
        p = e_p;
      }
    }
    ans += abs(current - p);
    m.erase(p);
    current = p;
  }

  cout << ans << '\n';
}
