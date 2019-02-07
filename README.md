[![Build Status](https://travis-ci.org/rt-net/raspicat_basic.svg?branch=master)](https://travis-ci.org/rt-net/raspicat_basic)

# raspicat_basic

「[Raspberry Piで学ぶ ROSロボット入門](https://www.nikkeibp.co.jp/atclpubmkt/book/17/261040/)」の6章から9章までをRaspberry Pi Catに対応させたプログラムです。

コードを書く際、上記書籍の`pimouse_ros`を`raspicat_basic`に読み替えながらプログラムを書くことで本リポジトリと同じプログラムが作成できるようになります。

そのほか本リポジトリでは[ryuichiueda/raspimouse_book_info](https://github.com/ryuichiueda/raspimouse_book_info)にて公開されている修正点を反映した状態で公開しています。

## 変更箇所

* パッケージ名
  * https://github.com/rt-net/raspicat_basic/commit/d8c5eaf3093f17874bfd1934055cd66e3f11943d
* Raspberry Pi Cat固有のパラメータ
  * https://github.com/rt-net/raspicat_basic/commit/aba93778b75032ed4466de39b67f967845c43456
* TravisCIでエラーが出る問題
  * https://github.com/rt-net/raspicat_basic/commit/1b3695b4ee794ee7f0b0e05360ee09b7b94e0dfc

### 固有のパラメータについて

Raspberry Pi CatはRasberry Pi Mouseとサイズが異なるため、指令された移動速度からモータへの指令を計算するためのノードに記述するパラメータが異なります。

* Raspberry Pi Mouse (「[Raspberry Piで学ぶ ROSロボット入門](https://www.nikkeibp.co.jp/atclpubmkt/book/17/261040/)」のP.279参照)
  * ホイール径: 45[mm]
  * トレッド: 90[mm]
* Raspberry Pi Cat
  * ホイール径: 150[mm]
  * トレッド: 280[mm]

![](https://raw.githubusercontent.com/rt-net/RaspberryPiCat_Hardware/master/drawing/RasPiCat_wheel_drawing.png)
