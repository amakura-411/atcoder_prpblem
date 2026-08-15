#include <bits/stdc++.h>

#include <cstdint>
#include <queue>
#include <vector>
using namespace std;

int main() {
  // ここにプログラムを追記
  int64_t q;
  int64_t v;
  priority_queue<int64_t, vector<int64_t>> que;
  cin >> q >> v;
  for (int i = 0; i < q; i++) {
    int o;
    cin >> o;
    if (o == 1) {
      int t;
      int w;
      cin >> t >> w;
      que.push(w - t);
    } else {
      int t;
      cin >> t;
      if (que.empty()) {
        cout << "-1" << '\n';
      } else {
        int64_t top = que.top();
        que.pop();
        int64_t ans = min(top + t, v);
        cout << ans << '\n';
      }
    }
  }
}
