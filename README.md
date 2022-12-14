# mypkg

![test](https://github.com/ahaya8810/mypkg/actions/workflows/test.yml/badge.svg)

このリポジトリはロボットシステム学で使用しているリポジトリです。

このリポジトリはROS2のパッケージです。

## talkerコマンド

### 機能

整数を０から順番にカウントしていく。

## listenerコマンド

### 機能

talkerがカウントした数字を取得して標準出力で出力する。

## 実行方法等

### 実行方法の例

以下の２つのコマンドは別々のターミナルで実行する

```
$ ros2 run mypkg talker
```
```
$ ros2 run mypkg listener
```
あるいは、以下のコードで実行することで、一つのターミナルで同時に実行できる。
```
$ ros2 launch mypkg talk_listen.launch.py
```
### 起動例1
talker側
```
$ ros2 run mypkg talker
```
listener側
```
$ ros2 run mypkg listener
[INFO] [1671701267.171804400] [listener]: Listen: 0
[INFO] [1671701267.672352000] [listener]: Listen: 1
[INFO] [1671701268.172334200] [listener]: Listen: 2
[INFO] [1671701268.672022600] [listener]: Listen: 3
[INFO] [1671701269.172308500] [listener]: Listen: 4
[INFO] [1671701269.672704900] [listener]: Listen: 5
[INFO] [1671701270.172425900] [listener]: Listen: 6
[INFO] [1671701270.672327900] [listener]: Listen: 7
....
```
### 起動例2
```
$ ros2 launch mypkg talk_listen.launch.py
[listener-2] [INFO] [1671768364.680333300] [listener]: Listen: 0
[listener-2] [INFO] [1671768365.140367600] [listener]: Listen: 1
[listener-2] [INFO] [1671768365.640273900] [listener]: Listen: 2
[listener-2] [INFO] [1671768366.140561700] [listener]: Listen: 3
[listener-2] [INFO] [1671768366.640282900] [listener]: Listen: 4
[listener-2] [INFO] [1671768367.140304000] [listener]: Listen: 5
[listener-2] [INFO] [1671768367.640747100] [listener]: Listen: 6
....
```
### 必要なソフトウェア
* ROS2
### テスト環境
* ubuntu 22.04.1 LTS
## 権利
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
