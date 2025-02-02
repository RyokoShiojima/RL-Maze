## 概要
強化学習を用いて, エージェントに自作の迷路を解かせる.

## 変更点
### map.py
| 何行目か       | 変更点                       | 説明                          | 
| -------------- | ---------------------------- | ----------------------------- | 
| 15行目〜27行目 | マップの拡張                 | (11,11)→(12,12)              | 
| 30行目〜32行目 | ゴールの増設                 | ゴール1つ→ゴール3つ          | 
| 68行目〜81行目 | ゴール, 凸凹通路の表示を追加 | 3つのゴール, 凸凹通路の可視化 | 

### agent.py
| 何行目か       | 変更点         | 説明                                               |
| -------------- | -------------- | -------------------------------------------------- |
| 2行目          | 引数の追加     | 増やしたゴールの座標を追加                         |
| 29行目〜32行目 | 終了判定の追加 | 増やしたゴールに着いた時に終了判定を返すように追加 |

### q-learning.py
 - 自分なりに書き換えました

 - 変更した機能

| 何行目か       | 変更点               | 説明                                                                                                                                                       | 
| -------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| 7行目〜14行目  | εグリーディ方策     | 自分なりにεグリーディ方策を実装してみました                                                                                                               | 
| 25行目〜53行目 | 報酬の変更           | エージェントがいるマスを座標に変換(3つのゴールでそれぞれ報酬が違うため),凸凹通路を定義, 凸凹通路を通った時の報酬, 増やしたゴールに辿り着いた際の報酬を定義 | 
| 55行目〜64行目 | 報酬の推移をプロット | 報酬の推移をプロットする関数の追加                                                                                                                         | 

## 動画
### 地図の見方
| 色           | 役割           | 説明                                  | 
| ------------ | -------------- | ------------------------------------- | 
| 黒           | 壁・行き止まり | エージェントが進めないマス            | 
| 緑           | スタート地点   | エージェントがepisodeの初めにいる場所 | 
| 青(○)       | ゴール1        | 一番良いゴール                        | 
| マゼンタ(△) | ゴール2        | まあまあなゴール                      | 
| シアン(✕)   | ゴール3        | 良くないゴール                        | 
| 灰色         | でこぼこ道     | 通るとマイナスになる道                | 
| 赤           | エージェント   | 学習対象                              | 
| 黄色         | 行動価値       | 色が濃いほど矢印方向の行動価値が高い  | 

### URL(Youtube)
- Q-Learning\
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/vxi46-EhQ_s/0.jpg)](https://youtu.be/vxi46-EhQ_s)


## 実行方法 (python)
```sh
$ git clone git@github.com:RyokoShiojima/RL-Maze.git
$ cd RL-Maze
$ python main.py 
```

## 実行方法 (jupyter notebook)
```sh
$ git clone git@github.com:RyokoShiojima/RL-Maze.git
$ cd RL-Maze/jupyter
$ jupyter notebook 
$ q-learning.ipynbを実行
```

## 必要となるライブラリ 
* matplotlib
* numpy
