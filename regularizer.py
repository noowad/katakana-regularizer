# coding:utf-8
import codecs

'''
カタカナの人名などを標準的なカタカナ表記に変換する時に使える。
基本的なルール
1.基本的にnon-standardにあるものはその通りに変換
2.小書きが入っているもの中でstandardに含まれていないものは小書きから大書きに変換
'''


def regularization(input_name):
    standards = codecs.open('./datas/standard.katakana', 'r', 'utf-8').read().splitlines()
    non_standard_list = codecs.open('./datas/non-standard.katakana', 'r', 'utf-8').read().splitlines()
    small_characters = {'ァ': 'ア', 'ィ': 'イ', 'ゥ': 'ウ', 'ェ': 'エ', 'ォ': 'オ', 'ャ': 'ヤ', 'ュ': 'ユ', 'ョ': 'ヨ'}
    non_standards = {}
    for non_standard in non_standard_list:
        pre = non_standard.split()[0]
        post = non_standard.split()[1]
        non_standards[pre] = post
    # 1
    for pre, post in non_standards.items():
        if pre in input_name:
            input_name = input_name.replace(pre, post)

    # 2
    for pre, post in small_characters.items():
        pre = codecs.decode(pre, 'utf-8')
        post = codecs.decode(post, 'utf-8')
        if pre in input_name:
            char = input_name[input_name.index(pre) - 1] + input_name[input_name.index(pre)]
            if char not in standards:
                input_name = input_name.replace(pre, post)
    return input_name
