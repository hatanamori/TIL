# REST API とは
Web APIの中でも「RESTのルールに従ったAPI」のこと
REST のルールとは：
- 資源（データ）を URL で表す
  - 例：`/users/1`
- 操作を HTTP メソッドで表す
  - GET / POST / PUT / DELETE / PATCH
- ステートレス（状態を持たない）
- 表現（JSON など）で送受信
REST は 統一されたルールで作られている ので使いやすい。

## 使い方
FastAPIというフレームワークを用いることで簡単に作成できる