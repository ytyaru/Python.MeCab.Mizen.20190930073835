#!/usr/bin/env python3
# coding: utf8
import Precaution
import Mizen
p = Precaution.Precaution()
mizen = Mizen.Mizen()

def prints(words):
    for word in words:
        if word is not None: print(word)

words = ['走る','押す','愛する','見る','食べる','来る']
for word in words:
    print('===== {} ====='.format(word))
    rows = p.get(word)
    for row in rows:
#        _not = mizen.get_not(row)
#        _not_old = mizen.get_not_old(row)
#        _conn = mizen.get_conn(row)
#        _special = mizen.get_not_special(row)
#        _reru = mizen.get_reru(row)
        mizens = (mizen.get_not(row),
                    mizen.get_not_old(row),
                    mizen.get_conn(row),
                    mizen.get_not_special(row),
                    mizen.get_reru(row))
        prints(mizens)

"""
print(p.get_conj_word('動く', '未然形'))
print(p.get_conjugations('動く'))
print(p.get_conj_word('動く', '未然形'))
print(p.get_conj_words('動く'))

mizen = Mizen.Mizen()
mizen.get_not()
mizen.get_not_old()
mizen.get_conn()
mizen.get_not_special()
mizen.get_reru()
"""
"""
定まる,772,772,6852,動詞,自立,*,*,五段・ラ行,基本形,定まる,サダマル,サダマル

0: 語(word)
1,2,3:
4: 品詞(word_class)
5: 単語種別(word_type)
6,7:
8: 活用種別(conj_type) 
9: 活用形種別(conj)
10: 語の基本形(word_base)
11,12: 読み？発音？
"""
