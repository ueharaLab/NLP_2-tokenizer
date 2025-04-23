import MeCab

tagger = MeCab.Tagger ('mecabrc') 
#tagger.parse('')# 実行の準備

token=tagger.parseToNode('いつもながら、パスタランチはお気軽でいい感じ。今回は2種類のパスタを2人でシェア盛りにしてもらいました。\
エビのオイルベースのショートパスタとトマトパスタ。あっさりした味付けで、いつの間にかペロリと食べてしまいます。お野菜を多く使ってヘルシーな内容 \
になっていました。ブルーベリージャムのババロアは定番なのだとか。いつ行っても食べられそうで嬉しいです。')

    
while token:
    print(token.surface,token.feature)
    token = token.next