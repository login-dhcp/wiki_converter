import re

expression = '############'

def func():
    str = '''
    SP	☆の数は解放に必要な特訓回数、E〇は〇番目のアイドルイベントで解放、灰色はライブスキル
20		Vocal7%UP	
[条件:4ターン以前]
[確率:20%]
[最大:1回]
30		Visual7%UP	ほわっとスマイル	
[条件:スター10以上]
[確率:30%]
[最大:1回]	Vocal&Visual
2倍アピール
(Link)Vocal&Visual
50%UP[4ターン]
40		Vocal&Dance40%UP
(☆2)	Vocal7%UP	Dance21%UP
(☆1)	
[条件:3ターン以前]
[確率:40%]
[最大:1回]	[条件:3位]
[確率:40%]
[最大:1回]	[条件:メンタル74%以下]
[確率:40%]
[最大:1回]
50	ほわっとスマイル+
(☆4)	Visual7%UP
(E4)	Dance上限UP	Vocal上限UP
(☆3)
Vocal&Visual
3倍アピール
(Link)Vocal&Visual
50%UP[4ターン]	[条件:観客3以上]
[確率:50%]
[最大:2回]	Dance上限+100	Vocal上限+200
    '''

    #parse(str)

    out = '''
{{틀:스킬 패널
| skill_20_1 = {{Vo}} 7% UP
| color_20_1 = {{Color_Dictionary | Vo_Background1}}
| effect_20_1 = [조건:4턴 이전]<br />[확률:20%]<br />[최대:1회]
| skill_30_1 = {{Vi}} 7% UP
| color_30_1 = {{Color_Dictionary | Vi_Background1}}
| effect_30_1 = [조건:스타 10 이상]<br />[확률:30%]<br />[최대:1회]
| skill_30_2 = ほわっとスマイル
| color_30_2 = {{Color_Dictionary | Gray_Background1}}
| effect_30_2 = {{Vo}} & {{Vi}} 2배 어필/<br />(Link) {{Da}} & {{Vi}} 50% UP[4턴]
| skill_40_1 = {{Da}} & {{Vi}} 40% UP / 주목도 40% UP(☆2)
| color_40_1 = {{Color_Dictionary | Gray_Background1}}
| effect_40_1 = [조건: 3턴 이전]<br />[확률:40%]<br />[最大:1회]
| skill_40_2 = {{Vo}} 7% UP
| color_40_2 = {{Color_Dictionary | Vo_Background1}}
| effect_40_2 = [조건: 3위]<br />[확률:40%]<br />[最大:1회]
| skill_40_3 = {{Da}} 21% UP(☆1)
| color_40_3 = {{Color_Dictionary | Da_Background1}}
| effect_40_3 = [조건: Me 74% 이하]<br />[확률:40%]<br />[最大:1회]
| skill_50_1 = ほわっとスマイル+(☆4)
| color_50_1 = {{Color_Dictionary | Gray_Background1}}
| effect_50_1 = {{Vo}} & {{Vi}} 3배 어필 <br />(Link) {{Vo}} & {{Vi}} 50% UP[4턴]
| skill_50_2 = {{Vi}} 7% UP(E4)
| color_50_2 = {{Color_Dictionary | Vi_Background1}}
| effect_50_2 = [조건: 관객 3 이상]<br />[확률:50%]<br />[最大:2회]
| skill_50_3 = {{Da}} 상한 UP
| color_50_3 = {{Color_Dictionary | Da_Background1}}
| effect_50_3 = {{Da}} 상한 +100
| skill_50_4 = {{Vo}} 상한 UP(☆3)
| color_50_4 = {{Color_Dictionary | Vo_Background1}}
| effect_50_4 = {{Vo}} 상한 +200
}}

    '''

    str2 = '''
    |BGCOLOR(sandybrown):CENTER:|>|>|>|>|>|>|>|CENTER:70|c
|~SP|>|>|>|>|>|>|>|~☆の数は解放に必要な特訓回数、E〇は〇番目のアイドルイベントで解放、灰色はライブスキル|
|~20|>|>||>|BGCOLOR(lightpink):~Vocal7%UP|>|>||
|~|~|~|~|>|[条件:4ターン以前]&br;[確率:20%]&br;[最大:1回]|~|~|~|
|~30|>||>|BGCOLOR(lemonchiffon):~Visual7%UP|>|~&color(,lightpink){ほわっと};&color(,lemonchiffon){スマイル};|>||
|~|~|~|>|[条件:スター10以上]&br;[確率:30%]&br;[最大:1回]|>|BGCOLOR(gainsboro):Vocal&Visual&br;2倍アピール&br;(Link)&color(,lightpink){Vocal};&&color(,lemonchiffon){Visual};&br;50%UP[4ターン]|~|~|
|~40||>|~&color(,lightpink){Vocal};&&color(,paleturquoise){Dance};40%UP&br;(☆2)|>|BGCOLOR(lightpink):~Vocal7%UP|>|BGCOLOR(paleturquoise):~Dance21%UP&br;(☆1)||
|~|~|>|[条件:3ターン以前]&br;[確率:40%]&br;[最大:1回]|>|[条件:3位]&br;[確率:40%]&br;[最大:1回]|>|[条件:メンタル74%以下]&br;[確率:40%]&br;[最大:1回]|~|
|~50|>|~&color(,lightpink){ほわっと};&color(,lemonchiffon){スマイル};+&br;(☆4)|>|BGCOLOR(lemonchiffon):~Visual7%UP&br;(E4)|>|BGCOLOR(paleturquoise):~Dance上限UP|>|BGCOLOR(lightpink):~Vocal上限UP&br;(☆3)|
|~|>|BGCOLOR(gainsboro):Vocal&Visual&br;3倍アピール&br;(Link)&color(,lightpink){Vocal};&&color(,lemonchiffon){Visual};&br;50%UP[4ターン]|>|[条件:観客3以上]&br;[確率:50%]&br;[最大:2回]|>|Dance上限+100|>|Vocal上限+200|
    '''

    parse2(str2)

def parse(str_input):
    out = '''{{틀:스킬 패널\n'''

    sps = []
    lines = str_input.strip().split()
    print(lines)

    sp = 20
    for i in range(len(lines)):
        line = lines[i]
        if str(sp) in line:
            sps.append((sp, i))
            sp += 10
    print(sps)


    skills = []
    for i in range(len(sps)-1):
        sp, start = sps[i]
        _, end = sps[i+1]

        cnt = 1
        effect = ''
        for j in range(start, end):
            print(sp, lines[j])
            if "条件" in lines[j]:
                add = f'| effect_{sp}_{cnt} = [조건: {lines[j].split("条件")[1]}]<br />'
                effect = add
            elif "確率" in lines[j]:
                add = f'[확률:{lines[j].split("確率")[1]}<br />'
                effect += add
            elif "最大" in lines[j]:
                add = f'[최대:{lines[j].split("最大")[1]}<br />\n'
                #add.replace()
                effect += add
                out += effect
                cnt += 1
            elif str(sp) == lines[j]:
                pass
            else:
                skills.append((lines[j], j, sp))

    sp, start = sps[-1]
    end = len(lines) -1
    cnt = 1
    effect = ''
    for j in range(start, end):
        print(sp, lines[j])
        if "条件" in lines[j]:
            add = f'| effect_{sp}_{cnt} = [조건: {lines[j].split("条件")[1]}]<br />'
            effect = add
        elif "確率" in lines[j]:
            add = f'[확률:{lines[j].split("確率")[1]}<br />'
            effect += add
        elif "最大" in lines[j]:
            add = f'[최대:{lines[j].split("最大")[1]}<br />\n'
            # add.replace()
            effect += add
            out += effect
            cnt += 1
        elif str(sp) == lines[j]:
            pass
        else:
            skills.append((lines[j], j, sp))

    print(out)
    print(skills)

    for i in range(len(skills)):
        skill = skills[i]

    #print(str_input.strip().split('\n'))


def parse2(str_input):

    out = '''== 스킬 패널 ==\n{{틀:스킬 패널\n'''

    sp = 20
    sps = []
    lines = str_input.strip().split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if f'~{sp}' in line:
            sps.append((sp, i))
            sp += 10

    for i in range(len(sps)):
        sp, start = sps[i]
        try:
            _, end = sps[i+1]
        except IndexError:
            end = len(lines)

        cnt_skill = 1
        cnt_effect = 1
        for j in range(start, end):
            line = lines[j]
            words = line.split('>')

            if f'~{sp}' in line:
                for word in words:
                    word = reg_replace(word)
                    if word == str(sp):
                        word = ''
                    if len(word) > 0:
                        add = f'| skill_{sp}_{cnt_skill} = ' + word + '\n'
                        out += add

                        det = 0
                        if 'Vo' in add or 'vo' in add:
                            det += 1
                        if 'Da' in add or 'da' in add:
                            det += 2
                        if 'Vi' in add or 'vi' in add:
                            det += 4

                        if det == 1:
                            color = '''{{Color_Dictionary | Vo_Background1}}'''
                        elif det == 2:
                            color = '''{{Color_Dictionary | Da_Background1}}'''
                        elif det == 4:
                            color = '''{{Color_Dictionary | Vi_Background1}}'''
                        else:
                            color = '''{{Color_Dictionary | Gray_Background1}}'''

                        add = f'| color_{sp}_{cnt_skill} = ' + color + '\n'
                        out += add

                        cnt_skill += 1
            else:
                for word in words:
                    word = reg_replace(word)
                    if len(word) > 5:
                        add = f'| effect_{sp}_{cnt_effect} = ' + word + '\n'
                        out += add
                        cnt_effect += 1

    out += '}}'
    #print(out)
    assert out.count('{') == out.count('}')
    return out



def reg_replace(word):
    # basic wiki expressions deletion
    word = re.sub('color([^{]*)', '', word)
    word = re.sub('BGCOLOR.*:', '', word)
    word = re.sub('\|', '', word)
    word = re.sub('~', '', word)
    word = re.sub('&br;', '<br />', word)

    # shiywiki expressions
    word = re.sub('vocal', '{{Vo}} ', word, flags=re.IGNORECASE)
    word = re.sub('dance', '{{Da}} ', word, flags=re.IGNORECASE)
    word = re.sub('visual', '{{Vi}} ', word, flags=re.IGNORECASE)

    # jp to kr
    word = re.sub('条件', '조건', word)
    word = re.sub('確率', '확률', word)
    word = re.sub('最大', '최대', word)
    word = re.sub('上限', '상한 ', word)
    word = re.sub('倍', '배 ', word)
    word = re.sub('アピール', '어필', word)
    word = re.sub('回', '회', word)
    word = re.sub('以上', '이상', word)
    word = re.sub('以下', '이하', word)
    word = re.sub('以前', '이전', word)
    word = re.sub('以降', '이후', word)
    word = re.sub('位', '위', word)
    word = re.sub('観客', '관객', word)
    word = re.sub('ターン', '턴 ', word)
    word = re.sub('スター', '스타  ', word)


    # other specific cases
    word = re.sub('<br />\(☆', ' (☆', word)
    word = re.sub('<br />\(E', ' (E', word)

    word = re.sub('};&&{', '& ', word)
    word = re.sub('};&{', ' ', word)  # &{ほわっと};&{スマイル};
    word = re.sub('};', '', word)
    word = re.sub('^&{', '', word)
    word = re.sub('<br />&{', '<br />', word)
    word = re.sub('<br />\(Link\)&{', '<br />(Link)', word)


    # styling
    word = re.sub('&{{', '& {{', word)

    #word =


    return word



if __name__ == '__main__':
    rarity = 'SR'

    inp = '''

|BGCOLOR(sandybrown):CENTER:|>|>|>|>|>|CENTER:70|c
|~SP|>|>|>|>|>|~☆の数は解放に必要な特訓回数、E〇は〇番目のアイドルイベントで解放、灰色はライブスキル|
|~20|>||>|BGCOLOR(lemonchiffon):~Visual4%UP|>||
|~|~|~|>|[条件:4ターン以降]&br;[確率:20%]&br;[最大:1回]|~|~|
|~30||>|BGCOLOR(paleturquoise):~Dance4%UP|>|~&color(,lemonchiffon){ハロー・};&color(,lightpink){ワールド};||
|~|~|>|[条件:スター10以上]&br;[確率:30%]&br;[最大:1回]|>|BGCOLOR(gainsboro):Visual1.5倍アピール/&br;Vocal0.5倍アピール&br;(Link)&color(,paleturquoise){Dance};1.5倍アピール|~|
|~40|>|BGCOLOR(lightpink):~Vocal30%UP(☆2)|>|BGCOLOR(lemonchiffon):~Visual4%UP(E1)|>|BGCOLOR(lightpink):~Vocal12%UP(☆1)|
|~|>|[条件:3ターン以降]&br;[確率:40%]&br;[最大:1回]|>|[条件:3位]&br;[確率:40%]&br;[最大:2回]|>|[条件:メンタル74%以下]&br;[確率:40%]&br;[最大:1回]|
|~50||>|~&color(,lightpink){ハロー・};&color(,paleturquoise){ワールド};+(☆4)|>|BGCOLOR(lightpink):~Vocal上限UP(☆3)||
|~|~|>|BGCOLOR(gainsboro):Vocal2倍アピール/&br;Dance1倍アピール&br;(Link)&color(,lemonchiffon){Visual};1.5倍アピール|>|Vocal上限+50|~|


    '''
    out = parse2(inp)

    if rarity == 'SR':
        out = re.sub('50_2', '50_3', out)
        out = re.sub('50_1', '50_2', out)


    print(out)


