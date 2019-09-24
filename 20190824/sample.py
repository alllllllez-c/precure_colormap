
#########################################################
#                                                       #
# iris データをプリキュアっぽい色で表示するテスト       #
#                                                       #
#########################################################


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# プリキュアカラーマップをインポート
import precure_colormap as pc

# style="whitegrid"：白背景＋グリッド
sns.set(style="whitegrid") 

# おなじみのiris(アヤメ)データのロード
iris = datasets.load_iris()

# DataFrameを構築 
# カラム名はデータに設定されてるのをそのまま使う(若干めんどいけど)
df = pd.DataFrame(data=iris.data, columns = iris.feature_names)

# プリキュアを呼ぶ準備
cure_colors = pc.cure_colormap()

# サイズ設定
# plt.figure(figsize=(12,9))

# 複数データ散布図
cc = cure_colors.get_by_name('キュアコスモ')
ax = df.plot.scatter(x='sepal length (cm)', y='sepal width (cm)', label='petal width (cm)', c=cc.colors[0], marker='s') # Listedなカラーマップはこれでとれる
ax = df.plot.scatter(x='sepal length (cm)', y='petal length (cm)', label='petal length (cm)', c=cc.colors[5], marker='o', ax=ax) 
ax = df.plot.scatter(x='sepal length (cm)', y='petal width (cm)', label='petal width (cm)', c=cc.colors[1], marker='*', ax=ax)
plt.legend()
plt.show()

# 相関係数でヒートマップ
sns.heatmap(df.corr(),linewidths=0.1, square=True, linecolor='white', annot=True, cmap=cure_colors.get_by_name('キュアフローラ'))
plt.show()

# 六角形ビニング図（hexbin plot）
# 散布図での六角形のエリアに入る点の数を色の濃さで表したグラフ 
# 背景まで塗っちゃうから、トーンが揃ってるか、先頭の色が薄いプリキュアじゃないと違和感
df.plot.hexbin(x='sepal length (cm)', y='petal length (cm)', gridsize=8, sharex=False, colormap=cure_colors.get_by_name('キュアトゥインクル'))
plt.show()
df.plot.hexbin(x='sepal length (cm)', y='petal length (cm)', gridsize=8, sharex=False, colormap=cure_colors.get_by_name('キュアアンフィニ')) # この配色が一番よい
plt.show()

# (プリキュアハッカソン LT後追記)
# 
# 違うクラスタの色の差があまりない場合が多くて、
# LTしながら「あまりいい使用例じゃないな。。。」と思った。というか言ってた。
# ごめんなさい、トワ様。
# 
# よくよく考えたら、キャラクターに使用する色合いってのは
# 調和が取れる色になっているわけで、
# 似た色で色分けしちちゃうことになる(結果見づらい)のは当たり前。
# 
# キュアコスモやキュアパルフェのように「七色」がキーカラーのプリキュアで色付するのがいいだろうと思いました。
