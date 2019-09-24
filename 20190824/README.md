# プリキュアっぽい配色でグラフを描いてみた


## はじめに

**仕事で使うものに、好きなキャラクターの要素を取り入れたい！**

好きなキャラクターのグッズとか、持っていたり机に置いているだけで、
ちょっと癒やされたり、だいぶテンション上がったりしますよね。

かくいう私もプリキュアが大好きで、仕事で使うもののどこかに、
プリキュア要素を紛れ込ませられないかな・・・と
常日頃、思考をめぐらせていました。

というわけで、プリキュアっぽい配色でグラフを描くためのクラス 
`cure_colormap` を作ってみました。


## ファイル構成

 * `README.md`
   * このファイル
 * `precure_colormap.py`
   * プリキュアっぽいカラーマップのソースファイル
 * `sample.py`
   * カラーマップの使用例ソースファイル


## 使い方

`$ pip install precure` はまだできない。すまんな。


### 使用例

[キュアトゥインクル](https://dic.pixiv.net/a/%E3%82%AD%E3%83%A5%E3%82%A2%E3%83%88%E3%82%A5%E3%82%A4%E3%83%B3%E3%82%AF%E3%83%AB)っぽい配色で描画します。[^1] 

![cure_twinkle](https://user-images.githubusercontent.com/13117729/65551912-ef39b580-df5d-11e9-96fc-1fea6c75a725.png)

```
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# プリキュアカラーマップをインポート
import precure_colormap

sns.set(style="whitegrid")
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data,
                  columns = iris.feature_names)
cure_colors = precure_colormap.cure_colormap()

df.plot.hexbin(x='sepal length (cm)', y='petal length (cm)',
               gridsize=10, sharex=False,
               colormap=cure_colors.get_by_name('キュアトゥインクル'))
plt.show()
```

![cure_twinkle_hexbin](https://user-images.githubusercontent.com/13117729/65551928-fa8ce100-df5d-11e9-94c8-93fa6c893a29.png)


## 参考資料

 * __＜プリキュアガーデン＞__
   * [http://www.toei-anim.co.jp/ptr/precure/](http://www.toei-anim.co.jp/ptr/precure/)
   * プリキュアの色は、基本的にキャラクター紹介ページの画像準拠です。
 * __＜ColorPick Eyedropper＞__
   * [https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg](https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg)
   * プリキュアの色取得に使用したツール。
 * __＜【Python】matplotlibによるグラフ描画時のColormapのカスタマイズ＞__  
   * [https://qiita.com/kenmatsu4/items/fe8a2f1c34c8d5676df8](https://qiita.com/kenmatsu4/items/fe8a2f1c34c8d5676df8)
 * __＜matplotlib - カラーマップについて＞__  
   * [http://pynote.hatenablog.com/entry/matplotlib-color](http://pynote.hatenablog.com/entry/matplotlib-color)
 * __＜プリキュアの英語名称＞__
   * [https://en.wikipedia.org/wiki/Pretty_Cure](https://en.wikipedia.org/wiki/Pretty_Cure)
 * __＜キュアっぽさは色味から。カラースキームを抽出してプリキュアっぽいカラーパレットを作ってみよう＞__
   * [https://www.gizmodo.jp/2017/05/precure-color-palette.html](https://www.gizmodo.jp/2017/05/precure-color-palette.html)
 * __＜LT資料＞__
   * [https://drive.google.com/open?id=1HAAok9Q4YBr-a7eSE18TqCTYex9qtDN-](https://drive.google.com/open?id=1HAAok9Q4YBr-a7eSE18TqCTYex9qtDN-)


[^1]: キュアトゥインクルを例として使った理由は、キュアトゥインクルが好きだからです。
