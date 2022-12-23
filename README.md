# mypkg

![test](https://github.com/ahaya8810/mypkg/actions/workflows/test.yml/badge.svg)

このリポジトリはロボットシステム学で使用しているリポジトリです。

## talkerコマンド

### 機能

整数を０から順番に宣言していく

## listenerコマンド

### 機能

talkerが宣言した数字を標準出力する

## 実行方法等

### 実行方法の例

以下の２つのコマンドは別々のターミナルで実行する

```
$ ros2 run mypkg talker
```
```
$ ros2 run mypkg listener
```
### 起動例
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
### 必要なソフトウェア
* Python 3
### テスト環境
* ubuntu 22.04.1 LTS
## 権利
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
