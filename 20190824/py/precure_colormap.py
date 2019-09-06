# coding: utf-8

# Pythonで使えるプリキュアっぽいカラーマップを作ってみました。
# 

# In[ ]:

# 必要なパッケージ
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

from collections import OrderedDict
# colormapをカスタマイズする
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap

import unittest

try:
    get_ipython().magic('matplotlib inline')
except:
    pass

# スタイル設定
# style="whitegrid"：白背景＋グリッド
# カラーパレットは指定しない(palette='deep'になる)
# color_codes=True：指定したパレットに簡略色コードを設定する('r'とか) # いる?
sns.set(style="whitegrid", color_codes=True) 


# ##  キュアップ・ラパパ！
# 
# 色よ、プリキュアカラーに変われ！
# 
# ・・・
# 
# プリキュアの魔法で、クラス `cure_colormap` が生み出されたようです。 
# 
# プリキュアの名前を呼ぶと、プリキュアっぽいカラーマップが返ってくるみたい！ワクワクもんだぁ！
# 「名前を呼ぶと」って言ってるんで、　インターフェースも要りますねえ
# 

# In[ ]:

class cure_colormap :
    '''
    プリキュアっぽいカラーマップを生成して取得するクラス
    
    Attributes
    ----------
    name_to_cmap : dictionary object
        プリキュアの名称 -> colormap への対応
    
    title_to_characters : OrderedDict object
       作品タイトルと登場プリキュアのマップ
    
    cure_black
    cure_white
    shiny_luminous
    ：
    <ALL Precure> : matplotlib.colors.Colormap object
        各プリキュアのカラーマップ
        
        TODO：直接呼び出したかったからこうしたけど、全プリキュア分のインスタンス保持しとくのはさすがに重くね？呼び出されたときでよくね？
    
    '''
    def __init__(self):
        self.name_to_cmap = dict()

        # ふたりはプリキュア
        # self.cure_black = self.generate_cure_cmap(['#00072A', '#00072A', '#842C72', '#FBFBFB', '#D49033', '#FF3398'], ['キュアブラック', 'Cure Black'], method=self.generate_cmap_q)
        self.cure_black = self.generate_cure_cmap(['#00072A', '#00072A', '#6e4001', '#FF3398', '#FBFBFB'], ['キュアブラック', 'Cure Black']) # TODO まだ何か違う
        # self.cure_white = self.generate_cure_cmap(['#F4F4F4', '#F4F4F4', '#78DDE4', '#0365B5', '#120c4f'], ['キュアホワイト', 'Cure White'], method=self.generate_cmap_q)
        self.cure_white = self.generate_cure_cmap(['#F4F4F4', '#F4F4F4', '#78DDE4', '#0365B5', '#120c4f'], ['キュアホワイト', 'Cure White']) # TODO 違う気がする

        # ふたりはプリキュア Max Heart
        self.shiny_luminous = self.generate_cure_cmap(['#FECF04', '#FEFB53', '#F5F7F7', '#FEB1D1', '#FE3521'], ['シャイニールミナス', 'Shiny Luminous'])

        # ふたりはプリキュア Splash Star
        self.cure_bloom = self.generate_cure_cmap(['#FCAC35', '#FFFF8E', '#FF3292', '#942953'], ['キュアブルーム', 'Cure Bloom'])
        self.cure_bright = self.generate_cure_cmap(['#FDAD38', '#FBCF84', '#FFFFA6', '#F0E947', '#97F518', '#FFFFDF', '#F93B9A', '#DC0067', '#942953'], ['キュアブライト', 'Cure Bright']) # 東映公式に大きめの画像がない？ # https://www.asahi.co.jp/precure_ss/character/img/cb.gif
        self.cure_eglet = self.generate_cure_cmap(['#711391', '#FFFFF3', '#D0D6FF', '#06FCD5'], ['キュアイーグレット', 'Cure Egret'])        
        self.cure_windy = self.generate_cure_cmap(['#741B93', '#711391', '#D16FE7', '#F8F8F8', '#FFF3FD', '#FDB2E1', '#DFFFFF', '#01FEDE'], ['キュアウインディ', 'Cure Windy']) # 東映公式に大きめの画像がない？ # https://www.asahi.co.jp/precure_ss/character/img/cw.gif
        self.kaoru_kiryuu = self.generate_cure_cmap(['#275D8A', '#DDECF1', '#E7F5FD', '#DDB9CB', '#CC87BB'], ['霧生薫', 'Kaoru Kiryuu']) # https://lohas.nicoseiga.jp/thumb/8016685i?1522857603
        self.michiru_kiryuu = self.generate_cure_cmap(['#8D2045', '#DC98A9', '#C5E462', '#FFEE2C', '#F9FA9B', '#C11E7A'], ['霧生満', 'Michiru Kiryuu']) # https://lohas.nicoseiga.jp/thumb/8016685i?1522857603

        # Yes!プリキュア5
        self.cure_dream = self.generate_cure_cmap(['#A6366B', '#F14694', '#FFB8F9', '#FFFBCD', '#FFFBCD', '#ECD01B'], ['キュアドリーム', 'Cure Dream'])
        self.cure_rouge = self.generate_cure_cmap(['#D34B32', '#EC9689', '#EC9689', '#FCEDFD', '#FCEDFD', '#FF1EA9'], ['キュアルージュ', 'Cure Rouge']) # 紫を入れたい #680CB1
        self.cure_lemonade = self.generate_cure_cmap(['#D8A725', '#FFEE9E', '#FAF4C2', '#FDFDF7', '#FAC04D', '#E39B14'], ['キュアレモネード', 'Cure Lemonade'])
        self.cure_mint = self.generate_cure_cmap(['#029476', '#55E5CD', '#FFFFF0', '#21AA03'], ['キュアミント', 'Cure Mint'])
        self.cure_aqua = self.generate_cure_cmap(['#1452A4', '#B3D3FE', '#F2FDFD', '#0974CC', '#3C3DA3'], ['キュアアクア', 'Cure Aqua'])
        
        self.dark_dream = self.generate_cure_cmap(['#D02674', '#F9D1EC', '#313144', '#000000'], ['ダークドリーム', 'Dark Dream'])
        self.dark_rouge = self.generate_cure_cmap(['#A92E3F', '#F8C8D6', '#313144', '#000000'], ['ダークルージュ', 'Dark Rouge'])
        self.dark_remonade = self.generate_cure_cmap(['#AB7221', '#FCD516', '#313144', '#000000'], ['ダークレモネード', 'Dark Lemonade'])
        self.dark_mint = self.generate_cure_cmap(['#05A67C', '#E1FEEF', '#313144', '#000000'], ['ダークミント', 'Dark Mint'])
        self.dark_aqua = self.generate_cure_cmap(['#366CCB', '#B9E8F8', '#313144', '#000000'], ['ダークアクア', 'Dark Aqua'])

        # Yes!プリキュア5GoGo!
        self.milky_rose = self.generate_cure_cmap(['#9136cf', '#CA2DA2', '#E7C8F9', '#B4EBEA', '#0386F3'], ['ミルキィローズ', 'Milky Rose'])

        # フレッシュプリキュア!
        self.cure_peach = self.generate_cure_cmap(['#953678', '#DC3E72', '#FF8ABF', '#FFF4AC'], ['キュアピーチ', 'Cure Peach'])
        self.cure_berry = self.generate_cure_cmap(['#353A57', '#2E7DCA', '#6AB7FE', '#C7B3FA'], ['キュアベリー', 'Cure Berry'])
        self.cure_pine = self.generate_cure_cmap(['#9B4750', '#FD8E18', '#FFDA5C', '#DB7A45'], ['キュアパイン', 'Cure Pine'])
        self.cure_passion = self.generate_cure_cmap(['#242B33', '#8E0331', '#DA2A3D', '#FFCBE5'], ['キュアパッション', 'Cure Passion'])
        
        # ハートキャッチプリキュア！
        self.cure_blossom = self.generate_cure_cmap(['#cf1b71', '#F954BD', '#FD98D7', '#FEF3FE'], ['キュアブロッサム', 'Cure Blossom'])
        self.cure_marine = self.generate_cure_cmap(['#4A7AED', '#6EB2F1', '#63DEED', '#EFFAFF'], ['キュアマリン', 'Cure Marine'])
        self.cure_sunshine = self.generate_cure_cmap(['#F98435', '#FFAC05', '#FFE55C', '#DD991D'], ['キュアサンシャイン', 'Cure Sunshine'])
        self.cure_moonlight = self.generate_cure_cmap(['#404A8F', '#6F7FDE', '#CDD5E2', '#D0B0D9'], ['キュアムーンライト', 'Cure Moonlight'])
        self.cure_flower = self.generate_cure_cmap(['#CE7AAE', '#F8D1EC', '#F9FCBF', '#FD9CBF', '#CB1C55'], ['キュアフラワー', 'Cure Flower']) # https://www.asahi.co.jp/heartcatch_precure/img/character/photo/flower.png
        self.dark_precure = self.generate_cure_cmap(['#171717', '#042F36', '#A6D8C6', '#FDA4BE', '#980E13'], ['ダークプリキュア', 'Dark Precure'])
        
        # スイートプリキュア♪
        self.cure_melody = self.generate_cure_cmap(['#DC3688', '#FF78C4', '#F9A5C9', '#FFFFFF'], ['キュアメロディ', 'Cure Melody'])
        self.cure_rhythm = self.generate_cure_cmap(['#D0A947', '#FDF48B', '#FAB7E5', '#FFFFFF'], ['キュアリズム', 'Cure Rhythm']) # まだやりようがある ＃ #FFFFFF が真ん中のほうがよくない？？？？
        self.cure_beat = self.generate_cure_cmap(['#303277', '#728CF1', '#C2EBFC', '#D393F8', '#FFFFFF'], ['キュアビート', 'Cure Beat'])
        self.cure_muse = self.generate_cure_cmap(['#C86424', '#FFAC4E', '#FACC2A', '#FFFB52', '#FFFFFF'], ['キュアミューズ', 'Cure Muse'])

        # スマイルプリキュア! 
        self.cure_happy = self.generate_cure_cmap(['#A62169', '#EB4CB0', '#FFFFFF'], ['キュアハッピー', 'Cure Happy'])
        self.cure_sunny = self.generate_cure_cmap(['#A42C04', '#F95000', '#FEFFD5'], ['キュアサニー', 'Cure Sunny'])
        self.cure_peace = self.generate_cure_cmap(['#D3A502', '#FDE552', '#FFFFEE'], ['キュアピース', 'Cure Peace'])
        self.cure_march = self.generate_cure_cmap(['#208635', '#4DDC50', '#F3FED6'], ['キュアマーチ', 'Cure March'])
        self.cure_beauty = self.generate_cure_cmap(['#3135A5', '#86A6FF', '#DAE7FA'], ['キュアビューティ', 'Cure Beauty'])

        # ドキドキ!プリキュア
        self.cure_heart = self.generate_cure_cmap(['#D4A615', '#FFF99E', '#FAFAFA', '#FAB1E2', '#EC3C9C'], ['キュアハート', 'Cure Heart'])
        self.cure_diamond = self.generate_cure_cmap(['#4245AF', '#A8ACF9', '#FAFAFA', '#5791F1', '#597AA7'], ['キュアダイヤモンド', 'Cure Diamond'])
        self.cure_rosetta = self.generate_cure_cmap(['#B3481E', '#FFC05C', '#FAFAFA', '#C9EFB6', '#F7DB3D'], ['キュアロゼッタ', 'Cure Rosetta'])
        self.cure_sword = self.generate_cure_cmap(['#AE57B5', '#EEB4F8', '#FAFAFA', '#ADBBF5', '#8B87B2'], ['キュアソード', 'Cure Sword'])
        self.cure_ace = self.generate_cure_cmap(['#A51318', '#FD757D', '#FFE8EC', '#FAFAFA', '#FFFFFF'], ['キュアハート', 'Cure Ace'])
        self.cure_sebastian = self.generate_cure_cmap(['#36424E', '#E0EBF1', '#DB0517', '#DB3FA2', '#F48484'], ['キュアセバスチャン', 'Cure Sebastian'])

        # ハピネスチャージプリキュア!
        self.cure_lovely = self.generate_cure_cmap(['#B51573', '#FB8DDE', '#FFE7FD', '#334463'], ['キュアラブリー', 'Cure Lovely'])
        self.cure_princess = self.generate_cure_cmap(['#3C558E', '#BEDBFF', '#FAEFAB', '#334463'], ['キュアプリンセス', 'Cure Princess'])
        self.cure_honey = self.generate_cure_cmap(['#F3A11E', '#FFD144', '#FFF0CC', '#334463'], ['キュアハニー', 'Cure Honey'])
        self.cure_fortune = self.generate_cure_cmap(['#756BD8', '#A79AF8', '#EAD3FF', '#334463'], ['キュアフォーチュン', 'Cure Fortune'])
        self.cure_tender = self.generate_cure_cmap(['#67729C', '#7A87B4', '#BFBDFE', '#354463'], ['キュアテンダー', 'Cure Tender']) # https://www.asahi.co.jp/precure/happiness/story/backnum_39.html
        self.cure_mirage = self.generate_cure_cmap(['#E34F4B', '#F06C7A', '#F1C3C6', '#354463'], ['キュアミラージュ', 'Cure Mirage']) # https://blogs.yahoo.co.jp/pkrgn012/folder/519751.html?m=lc&p=1

        # Go!プリンセスプリキュア
        self.cure_flora = self.generate_cure_cmap(['#DC3482', '#FE8ADA', '#FFF5FD', '#F8F5A2'], ['キュアフローラ', 'Cure Flora'])
        self.cure_marmaid = self.generate_cure_cmap(['#3C57D8', '#8EE9D8', '#F1FBF2', '#FCC3DD'], ['キュアマーメイド', 'Cure Mermaid'])
        self.cure_twinkle = self.generate_cure_cmap(['#F15312', '#FF9A18', '#FDFF94', '#FCE92D', '#BA70F8'], ['キュアトゥインクル', 'Cure Twinkle'])
        self.cure_scarlet = self.generate_cure_cmap(['#E73F94', '#FEC8FC', '#F6D437', '#E01646'], ['キュアスカーレット', 'Cure Scarlet'])        

        # 魔法つかいプリキュア!
        self.cure_miracle = self.generate_cure_cmap(['#E53972', '#F05EB1', '#FED6F5', '#FFE36F', '#F08A6A'], ['キュアミラクル', 'Cure Miracle']) # ダイヤスタイルで統一
        self.cure_magical = self.generate_cure_cmap(['#575E60', '#6A509D', '#8F79B5', '#AC7BB3', '#DE1A3F'], ['キュアマジカル', 'Cure Magical']) # ダイヤスタイルで統一
        self.cure_felice = self.generate_cure_cmap(['#FF649F', '#FFC8E7', '#FBFBF8', '#FFF75F', '#FBFBF8', '#D6FBEC', '#54E0A3'], ['キュアフェリーチェ', 'Cure Felice'])
        self.cure_mofurun = self.generate_cure_cmap(['#E37EAF', '#F8BA66', '#F29118', '#fff259', '#AD7BB3'], ['キュアモフルン', 'Cure Mofurun'])

        # キラキラ☆プリキュアアラモード
        self.cure_whip = self.generate_cure_cmap(['#A40945', '#FF488D', '#FEBDCA', '#F7EEB5'], ['キュアホイップ', 'Cure Whip'])
        self.cure_custard = self.generate_cure_cmap(['#BB3E26', '#FFF324', '#F9F9CF', '#FD663E'], ['キュアカスタード', 'Cure Custard'])
        self.cure_gelato = self.generate_cure_cmap(['#5959C9', '#3F6BEC', '#6CCDFF', '#FDFCDB'], ['キュアジェラート', 'Cure Gelato'])
        self.cure_macalon = self.generate_cure_cmap(['#F528AF', '#8B51D9', '#FBD2ED', '#D166D1'], ['キュアマカロン', 'Cure Macaron'])
        self.cure_chocolat = self.generate_cure_cmap(['#623114', '#986147', '#D80014', '#FFE9C2'], ['キュアショコラ', 'Cure Chocolat'])
        self.cure_parfait = self.generate_cure_cmap(['#FFC4EA', '#D21953', '#FF4766', '#FFA523', '#F5F78A', '#55F897', '#4FDBE8'], ['キュアパルフェ', 'Cure Parfait'], method=self.generate_cmap_q)
        self.cure_pekorin = self.generate_cure_cmap(['#DA064C', '#FF8AB4', '#F5CD5F', '#F3EBC1'], ['キュアペコリン', 'Cure Pekorin'])

        # HUGっと！プリキュア
        self.cure_yell = self.generate_cure_cmap(['#B30D39', '#F457A4', '#FEE0FE', '#A4EFCF', '#FEF395'], ['キュアエール', 'Cure Yell'])
        self.cure_ange = self.generate_cure_cmap(['#07A4FD', '#0EC9FE', '#A2EEFE', '#B9C9FB', '#FFF29C'], ['キュアアンジュ', 'Cure Ange'])
        self.cure_etoile = self.generate_cure_cmap(['#EFAB17', '#F7D95D', '#FFFB86', '#FFAD0C', '#6796EB'], ['キュアエトワール', 'Cure Etoile'])
        self.cure_macherie = self.generate_cure_cmap(['#DA003B', '#FF4D6F', '#FF8AAE', '#FF6FBB', '#F56AD5', '#FAFAA0'], ['キュアマシェリ', 'Cure Macherie'])
        self.cure_amour = self.generate_cure_cmap(['#B9C0FF', '#BC80E6', '#E35EEA', '#9044B0', '#FF5DC0'], ['キュアアムール', 'Cure Amour'])
        self.cure_anfini = self.generate_cure_cmap(['#C5E8E1', '#F4F5F9', '#FCEDB3', '#CDD7FE', '#A3A8E7'], ['キュアアンフィニ', 'Cure Anfini'])
        self.cure_tomorrow = self.generate_cure_cmap(['#FE1D79', '#FF98C2', '#FFD4ED', '#7CBFF3', '#FFF28F'], ['キュアトゥモロー', 'Cure Tomorrow']) # http://neoapo.com/characters/33689

        # スター☆トゥインクルプリキュア
        self.cure_star = self.generate_cure_cmap(['#E94471', '#F04878', '#FEE0F1', '#FFF6C0', '#FFE354'], ['キュアスター', 'Cure Star'])
        self.cure_milky = self.generate_cure_cmap(['#1E5DF6', '#16C1D0', '#BDF7FF', '#FEFFC0', '#FBE950'], ['キュアミルキー', 'Cure Milky'])
        #self.cure_soleil = self.generate_cure_cmap(['#C659AC', '#FF8E20', '#FFBE2C', '#FFF599', '#FFDE3A'], ['キュアソレイユ', 'Cure Soleil'])
        self.cure_soleil = self.generate_cure_cmap(['#C659AC', '#DB70A6', '#E26B14', '#FFBE2C', '#FFDE3A', '#FFF599'], ['キュアソレイユ', 'Cure Soleil'])
        self.cure_selene = self.generate_cure_cmap(['#8969DA', '#AA96FF', '#CDA5FD', '#E8FDFF', '#FEFA70'], ['キュアセレーネ', 'Cure Selene'])
        self.cure_cosmo = self.generate_cure_cmap(['#4F78FF', '#8AF0FC', '#B3FF7A', '#FFE63A', '#FF9D27', '#FF72D6', '#CD55ED', '#474969'], ['キュアコスモ', 'Cure Cosmo'], method=self.generate_cmap_q)


        # 作品タイトルと登場プリキュアのマップ
        self.title_to_characters = OrderedDict()

        # ふたりはプリキュア
        self.title_to_characters['Futari wa Pretty Cure'] = [
            'Cure Black',
            'Cure White'
        ]

        # ふたりはプリキュア Max Heart
        self.title_to_characters['Futari wa Pretty Cure Max Heart'] = [
            'Cure Black',
            'Cure White',
            'Shiny Luminous'
        ]

        # ふたりはプリキュア Splash Star
        self.title_to_characters['Futari wa Pretty Cure Splash Star'] = [
            'Cure Bloom',
            'Cure Bright',
            'Cure Egret',
            'Cure Windy',
            'Kaoru Kiryuu', #霧生薫
            'Michiru Kiryuu', #霧生満
        ]

        # Yes!プリキュア5
        self.title_to_characters['Yes! PreCure 5'] = [
            'Cure Dream',
            'Cure Rouge',
            'Cure Lemonade',
            'Cure Mint',
            'Cure Aqua',
            'Dark Dream',
            'Dark Rouge',
            'Dark Lemonade',
            'Dark Mint',
            'Dark Aqua'
        ]

        # Yes!プリキュア5GoGo!
        self.title_to_characters['Yes! PreCure 5 GoGo!'] = [
            'Cure Dream',
            'Cure Rouge',
            'Cure Lemonade',
            'Cure Mint',
            'Cure Aqua',
            'Milky Rose'
        ]

        # フレッシュプリキュア!
        self.title_to_characters['Fresh Pretty Cure!'] = [
            'Cure Peach',
            'Cure Berry',
            'Cure Pine',
            'Cure Passion'
        ]

        # ハートキャッチプリキュア！
        self.title_to_characters['HeartCatch PreCure!'] = [
            'Cure Blossom',
            'Cure Marine',
            'Cure Sunshine',
            'Cure Moonlight',
            'Cure Flower',
            'Dark Precure'
        ]

        # スイートプリキュア♪
        self.title_to_characters['Suite PreCure'] = [
            'Cure Melody',
            'Cure Rhythm',
            'Cure Beat',
            'Cure Muse'
        ]

        # スマイルプリキュア!
        self.title_to_characters['Smile PreCure!'] = [
            'Cure Happy',
            'Cure Sunny',
            'Cure Peace',
            'Cure March',
            'Cure Beauty',
        ]

        # ドキドキ!プリキュア
        self.title_to_characters['DokiDoki! PreCure'] = [
            'Cure Heart',
            'Cure Diamond',
            'Cure Rosetta',
            'Cure Sword',
            'Cure Ace',
            'Cure Sebastian',
        ]

        # ハピネスチャージプリキュア!
        self.title_to_characters['HappinessCharge PreCure!'] = [
            'Cure Lovely',
            'Cure Princess',
            'Cure Honey',
            'Cure Fortune',
            'Cure Tender',
            'Cure Mirage'
        ]

        # Go!プリンセスプリキュア
        self.title_to_characters['Go! Princess PreCure'] = [
            'Cure Flora',
            'Cure Mermaid',
            'Cure Twinkle',
            'Cure Scarlet'
        ]

        # 魔法つかいプリキュア!
        self.title_to_characters['Witchy PreCure!'] = [
            'Cure Miracle',
            'Cure Magical',
            'Cure Felice',
            'Cure Mofurun'
        ]

        # キラキラ☆プリキュアアラモード
        self.title_to_characters['Kirakira PreCure a la Mode'] = [
            'Cure Whip',
            'Cure Custard',
            'Cure Gelato',
            'Cure Macaron',
            'Cure Chocolat',
            'Cure Parfait',
            'Cure Pekorin'
        ]

        # HUGっと！プリキュア
        self.title_to_characters['Hugtto! PreCure'] = [
            'Cure Yell',
            'Cure Ange',
            'Cure Etoile',
            'Cure Macherie',
            'Cure Amour',
            'Cure Anfini',
            'Cure Tomorrow'
        ]

        # スター☆トゥインクルプリキュア
        self.title_to_characters['Star Twinkle PreCure'] = [
            'Cure Star',
            'Cure Milky',
            'Cure Soleil',
            'Cure Selene',
            'Cure Cosmo',
        ]

    def get_by_name(self, name):
        '''
        プリキュアの名前を受取り、対応するカラーマップを返す
        
        Parameter
        ---------
        name : string [in]
            プリキュアの名称
        
        Return
        ------
        matplotlib.colors.Colormap object
        一致するプリキュアがいなければNone
        
        '''
        return self.name_to_cmap.get(name)
    

    def generate_cmap(self, colors):
        '''
        指定した色でのカラーマップを返す

        Parameter
        ---------
        colors : array of color hexcode
            色の配列。色は16進数数か色名で指定。

        Return
        ------
        matplotlib.colors.Colormap object

        '''

        values = range(len(colors))

        vmax = np.ceil(np.max(values))
        color_list = []
        for v, c in zip(values, colors):
            color_list.append( ( v / vmax, c) )
        return LinearSegmentedColormap.from_list('custom_cmap', color_list)
    
    def generate_cmap_q(self, colors) :
        '''
        指定した色で、Qualitative(質的)なカラーマップを生成して返す
        
        Parameter
        ---------
        colors : array of color hexcode
        色の配列。色は16進数数か色名で指定。

        Return
        ------
        matplotlib.colors.Colormap object かな？
        
        '''
        return ListedColormap(sns.color_palette(colors).as_hex())

    def generate_cure_cmap(self, colors, names, method=None):
        '''
        指定した配色でカラーマップを生成し、
        プリキュアの名称と対応付ける
        
        Parameters
        ---------
        colors : array of color (hexcode or color name) [in]
            色の配列。色は16進数数か色名で指定。
        
        names : array of string [in]
            プリキュアの名前。

        method : function [in]
            カラーマップを生成する関数。matplotlib.colors.Colormap を返すもの。
            generate_cmap か generate_cmap_q

        Returns
        ------
        matplotlib.colors.Colormap 
            プリキュアカラーマップのオブジェクト。
        '''
        if method is None:
            method = self.generate_cmap
        
        if len(colors) < 1:
            return None
        
        cmap = method(colors)
        for name in names:
            self.name_to_cmap[name] = cmap
        
        return cmap

    def plot_color_maps(self, cmap_category, cmap_list):
        '''
        指定したカラーマップを一覧表示する。表示の際「カテゴリ名」を掲出

        '''
        # 表示するデータとして (1, 256) の配列を作成する。
        gradient = np.linspace(0, 1, 256).reshape(1, -1)

        cure_colors = self
        num_cmap_list = len(cmap_list)
        fig, axes = plt.subplots(num_cmap_list, 1, figsize=(9, num_cmap_list * 0.35))
        fig.subplots_adjust(wspace=0.4)
        axes[0].set_title(cmap_category + ' colormaps', fontsize=14, x=0.5)
        
        def plot_color_map(ax, gradient, name):
            cmap = cure_colors.get_by_name(name) 
            if cmap is None:
                return
            
            ax.imshow(gradient, aspect='auto', cmap=cmap)
            ax.set_axis_off()
            ax.text(-10, 0, name, va='center', ha='right', fontsize=10)
        
        for ax, name in zip(axes, cmap_list):
            plot_color_map(ax, gradient, name)
            # plot_color_map(axR, gradient, name + '_r') # 逆向きは作っていないので、上の表示も順方向だけのものに変更

    def sample_colormap_by_title(self, titles):
        '''
        指定した作品のカラーマップを表示
        '''
        for title in titles:
            cmap_list = self.title_to_characters.get(title)
            if cmap_list is None:
                continue
            
            self.plot_color_maps(title, cmap_list)

    def sample_colormap_all(self):
        '''
        全カラーマップ表示

        Parameter
        ---------
        None

        Return
        ------
        None

        '''
        
        for cmap_category, cmap_list in self.title_to_characters.items():
            self.plot_color_maps(cmap_category, cmap_list)

        plt.show()

# In[ ]:

## テスト
class test_cure_colormap(unittest.TestCase) :
    # def __init__(self, *args, **argc):
    #    super(test_cure_colormap, self).__init__()
    #    self.cure_colors = cure_colormap()
    cure_colors = cure_colormap()

    def setUp(self):
        # 初期化処理
        pass
    
    def tearDown(self):
        # 終了処理
        del self.cure_colors
    
    def test_generate_cure_cmap(self):
        # TODO　：　テスト関数を分けよう
        # カラーマップ生成関数
        # 色指定がないので生成しない
        cmap = self.cure_colors.generate_cure_cmap([], [])
        self.assertEqual(cmap, None, msg='Assert: generate_cure_cmap([], []) is NOT None')
        
        # 1色なので生成しない
        cmap = self.cure_colors.generate_cure_cmap( ['black'], [])
        self.assertEqual(cmap, None, msg="Assert: generate_cure_cmap(['black'], []) is NOT None")

        # 生成する
        cmap = self.cure_colors.generate_cure_cmap( ['black', 'white'], [], method=self.cure_colors.generate_cmap)
        self.assertIsInstance(cmap, LinearSegmentedColormap, msg="Assert: generate_cure_cmap(['black', 'white'], []) type is NOT matplotlib.colors.LinearSegmentedColormap")

        cmap = self.cure_colors.generate_cure_cmap( ['black', 'white'], [], method=self.cure_colors.generate_cmap_q)
        self.assertIsInstance(cmap, ListedColormap, msg="Assert: generate_cure_cmap(['black', 'white'], []) type is NOT matplotlib.colors.ListedColormap")

    def test_get_by_name(self):
        # メンバ直打ち
        self.assertIsNotNone(self.cure_colors.cure_twinkle, msg="ERROR: cure_colors.cure_twinkle is None" )
        # 名前で呼ぶ
        self.assertIsNotNone(self.cure_colors.get_by_name('キュアトゥインクル'), msg="ERROR: cure_colors.get_by_name('キュアトゥインクル') is None")
        # Noneに軟着陸する
        self.assertIsNone(self.cure_colors.get_by_name('キュアゴリラ'), msg="ERROR: cure_colors.get_by_name('キュアゴリラ') is None")

    def test_sample_colormap_all(self):
        self.cure_colors.sample_colormap_all()

    def test_sample_colormap_by_title(self, categories):
        self.cure_colors.sample_colormap_by_title(categories)

    def test_sample_iris(self):
        from sklearn import datasets
        # おなじみのiris(アヤメ)データのロード
        iris = datasets.load_iris()
        
        # DataFrameを構築 
        # カラム名はデータに設定されてるのをそのまま使う(若干めんどい)
        df = pd.DataFrame(data=iris.data, columns = iris.feature_names)

        # プリキュアを呼ぶ
        cure_colors = cure_colormap()

        fig = plt.figure(figsize=(13,7))
        df.plot.line(x='sepal length (cm)', style=['o', '*', 's'], colormap=cure_colors.cure_cosmo)
        plt.show()

        plt.figure(figsize=(12,9)) # サイズ設定 
        df.plot.hexbin(x='sepal length (cm)', y='petal length (cm)', gridsize=15, sharex=False, colormap=cure_colors.cure_twinkle)
        # (LT後追記)
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



# VScode debug
if __name__ != '__Main__':
    test = test_cure_colormap()
    #test.test_sample_colormap_all()
    test.test_sample_colormap_by_title(['Futari wa Pretty Cure'])
    test.test_sample_iris()


if __name__ == '__Main__':
    unittest.main(verbosity=2)




# # 参考資料
# 
# 
#  * __＜【Python】matplotlibによるグラフ描画時のColormapのカスタマイズ＞__  
#     [https://qiita.com/kenmatsu4/items/fe8a2f1c34c8d5676df8](https://qiita.com/kenmatsu4/items/fe8a2f1c34c8d5676df8)
#  * __＜matplotlib - カラーマップについて＞__  
#     [http://pynote.hatenablog.com/entry/matplotlib-color](http://pynote.hatenablog.com/entry/matplotlib-color)
#     

# # その他
# 
# 
# ## プリキュアの名称について
# 
#  * 英語名とメンバ変数名は[英語版Wikipedia](https://en.wikipedia.org/wiki/Pretty_Cure)準拠
# 
# ### 色の採り方について
# 
#  * 「[プリキュアガーデン](http://www.toei-anim.co.jp/ptr/precure/)」以下の各作品ページにある
#    キャラクター紹介ページの画像から抽出
#    * 「髪の毛の色」、「衣装の色」で構成してます
#    * ただしSSは絵が足りなかったので[朝日放送のページ](https://www.asahi.co.jp/precure_ss/)から
#      ・・・と思ったけどキュアブライトとキュアウインディが載ってなかった。えぇ・・・
#  * Chrome拡張「ColorPick Eyedropper」を使用して取得
#    * 配布は[こちら](https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg)
# 
# ### 追加の資料情報
# 
#  * [＜キュアっぽさは色味から。カラースキームを抽出してプリキュアっぽいカラーパレットを作ってみよう＞ ](https://www.gizmodo.jp/2017/05/precure-color-palette.html)
#    * 見落としていた先行研究。ありがたい！
# 



#%%
