import sys
import argparse


def split_small(inp, idol_name='사쿠라기_마노', type='P', rarity='SSR', card_num=1):
    inp = inp.strip()
    lines = inp.split('\n')

    commu_name = lines[0]

    cnt = 0
    for i in range(len(lines)):
        if 'SP' in lines[i]:
            cnt = i + 1
            break



    selects = lines[cnt:]
    stat_names = ['Vo', 'Da', 'Vi', 'Me', 'SP']
    me = ''
    sp = ''

    issmall = 'small' if len(selects) == 1 else ''

    out = f'{{{{틀: 커뮤 요약 {issmall}\n'
    out += f'| CommuNameJP = [[{idol_name}/{type}/{rarity}-{card_num}/{commu_name} | {commu_name}]]\n'
    out += f'| CommuNameKR = {commu_name}\n'


    for i in range(len(selects)):
        select = selects[i]
        stats = select.split('\t')

        s = stats[0]
        out += f'| Choice{i + 1}_JP = {s}\n'
        out += f'| Choice{i + 1}_KR = {s}\n'
        for j in range(1, len(stats)):
            if stats[j] != '':
                out += f'| Choice{i + 1}_{stat_names[j - 1]} = {stats[j].split("+")[-1]}\n'
                if j == 4:
                    me = stats[j].split('+')[-1]
                elif j == 5:
                    sp = stats[j].split('+')[-1]

        if i >= 1 and len(stats) < 5:
            out += f'| Choice{i + 1}_{stat_names[3]} = {me}\n'
            out += f'| Choice{i + 1}_{stat_names[4]} = {sp}\n'

    out += '}}'

    return out


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--input', type=str)
    # parser.add_argument('--idol_name', type=str)
    # parser.add_argument('--type', type=str)
    # parser.add_argument('--rarity', type=str)
    #
    # args = parser.parse_args()
    # out = split_small(args.input, args.idol_name, args.type, args.rarity)
    inp = '''
おひさまと布
冒頭	プロデューサー「――……霧子」
選択肢	Vo	Da	Vi	メンタル	SP
なし		+15	+15	+10	+20


    '''
    idol_name = '유코쿠 키리코'
    ctype = 'P'
    rarity = 'SR'
    card_num = 4
    out = split_small(inp, idol_name, ctype, rarity, card_num)
    print(out)
