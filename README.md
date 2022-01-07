## 概要
強化学習を用いて, エージェントに自作の迷路を解かせます.

## 動画

### 地図の見方

+ 黒・・・・・壁, エージェントはこのますに進むことができない. 
+ 緑・・・・・スタート地点, エージェントがepisodeの初めにいる場所
+ 青・・・・・ゴール地点, エージェントがここに達すると迷路を解いたことになる. 
+ 赤・・・・・エージェントの現在地
+ 黄・・・・・行動価値を可視化したもの, 色が濃いほど矢印方向の行動価値が高いことを示す.

### URL(Youtube)
+ Q-Learning  
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/TZWBzFWhU5k/0.jpg)](http://www.youtube.com/watch?v=TZWBzFWhU5k)  

+ SARSA  
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/rj-Hsv4iHUQ/0.jpg)](http://www.youtube.com/watch?v=rj-Hsv4iHUQ)  


## 実行方法 (python)
```sh
$ git clone https://github.com/matsumotokoki/probrobotics2021.git
$ cd probrobotics2021
$ python <実行するアルゴリズム>.py 
```

## 実行方法 (jupyter notebook)
```sh
$ git clone https://github.com/matsumotokoki/probrobotics2021.git
$ cd probrobotics2021/jupyter
# 上記2つのコマンド実行後, jupyterディレクトリでjupyter notebookを起動し, 実行したいアルゴリズムを実行
```

## 必要となるライブラリ 
* matplotlib
* numpy
* gym
