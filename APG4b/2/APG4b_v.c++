#include <bits/stdc++.h>
using namespace std;

int complete_time(vector<vector<int>> &children, int x) {
  // (ここに追記して再帰関数を実装する)
  // 1.「引数」「返り値」「処理内容」を決める
  // 引数	それぞれの組織の子組織一覧, 組織の番号
  // 返り値	最も遅く報告書を送る組織の報告書が揃う時刻
  // 処理内容	階層が最も深い子組織の報告書が揃う時刻を求める

  //階層が最も深い子組織の報告書が揃う時刻を求める
  // 再帰ステップ: 子組織の報告書が揃う時刻の最大値に1を足す
  // int s = 0;
  int s = 0;
  if(children.at(x).size() == 0) {
    return 0;
  }

  int max_time = 0;
  for(int i = 0; i < children.at(x).size(); i++) {
    // cout << "children.at(x).at(i): " << children.at(x).at(i) << " ";
    s = complete_time(children, children.at(x).at(i));
    // cout << "max_time, s:" << max_time << " " << s << " " << endl;
    max_time = max(max_time, s);
  }
  // cout << "max_time: " << max_time << " ";
  // cout << endl;

  return max_time + 1;

  // int s = complete_time(children, children.at(x).at(0));
  // return s + 1;
}

int main() {
  // ここにプログラムを追記
  //A社はN個の組織からなり、それぞれに0番からN−1番の番号が付いています
  // N - 1個の組織には必ず1つの親組織がある 1:多 子組織は複数
  // それぞれの組織は直接的または間接的にトップの組織と関係がある
  // 各組織は子組織の報告書がそろったら、自身の報告書を加えて親組織に送る
  // 子組織が無いような組織は自身の報告書だけをすぐに親組織に送ります

//   ある組織から報告書を送ってから、その親組織が受け取るときにかかる時間を1分とします。
// あるタイミングで一斉に報告書の伝達を開始したときに、
// トップの組織の元に全ての組織の報告書が揃う時刻（伝達を始めてから何分後か）を求めてください。 
// なお、各組織の報告書は既に準備されているため、報告書の伝達以外の時間はかからないこととします。

// 6
// 0 0 1 1 4
  int N;
  cin >> N;
  vector<int> p(N);
  p.at(0) = -1;  // 0番組織の親組織は存在しないので-1を入れておく
  for (int i = 1; i < N; i++) {
    cin >> p.at(i);
  }
  // 組織の関係から2次元配列を作る(理解しなくてもよい)
    vector<vector<int>> children(N);  // ある組織の子組織の番号一覧  // N×0の二次元配列
  for (int i = 1; i < N; i++) {
    int parent = p.at(i);  // i番の親組織の番号
    children.at(parent).push_back(i);  // parentの子組織一覧にi番を追加
  }
  // これで、各組織の子組織一覧が完成した
  cout << complete_time(children, 0) << endl;
}


