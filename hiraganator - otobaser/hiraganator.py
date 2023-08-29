import os

def convert_to_hiragana(text):
    hiragana_map = {
        'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
        'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
        'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
        'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
        'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
        'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
        'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
        'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
        'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
        'wa': 'わ', 'wo': 'を', 'n': 'ん',
        'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
        'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
        'da': 'だ', 'di': 'でぃ', 'zu': 'どぅ', 'de': 'で', 'do': 'ど',
        'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
        'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
        'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
        'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
        'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
        'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
        'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
        'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
        'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
        'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
        'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
        'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
        'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
        'bye': 'びぇ', 'che': 'ちぇ', 'di': 'でぃ', 'du': 'どぅ',
        'fa': 'ふぁ', 'fi': 'ふぃ', 'fe': 'ふぇ', 'fo': 'ふぉ',
        'fya': 'ふゃ', 'fyu': 'ふゅ', 'fye': 'ふぃぇ', 'fyo': 'ふょ',
        'hu': 'ほぅ', 'gye': 'ぎぇ', 'hye': 'ひぇ', 'je': 'じぇ',
        'kye': 'きぇ', 'mye': 'みぇ', 'nye': 'にぇ', 'pye': 'ぴぇ',
        'rye': 'りぇ', 'she': 'しぇ', 'tsa': 'つぁ', 'tsi': 'つぃ',
        'tse': 'つぇ', 'tso': 'つぉ', 'tyu': 'てゅ', 'dyu': 'でゅ',
        'va': 'ヴぁ', 'vi': 'ヴぃ', 'vu': 'ヴ', 've': 'ヴぇ', 'vo': 'ヴぉ',
        'vya': 'ヴゃ', 'vyu': 'ヴゅ', 'vye': 'ヴぇ', 'vyo': 'ヴょ',
        'wi': 'うぃ', 'we': 'うぇ', 'ye': 'いぇ', 'si': 'すぃ', 'zi': 'ずぃ',
        'ti': 'てぃ', 'tu': 'とぅ',
    }

    # Split the text by commas
    parts = text.split(',')
    # Convert the first part to Hiragana
    converted_text = hiragana_map.get(parts[0], parts[0])
    # Join the converted text with the remaining parts
    converted_text += ',' + ','.join(parts[1:])
    return converted_text

file_name = "oto.ini"
output_file_name = "oto_hiragana.ini"

with open(file_name, 'r') as file:
    lines = file.readlines()

converted_lines = []
for line in lines:
    if '=' in line:
        key, value = line.split('=')
        converted_value = convert_to_hiragana(value.strip())
        converted_line = f"{key}={converted_value}\n"
        converted_lines.append(converted_line)
    else:
        converted_lines.append(line)

with open(output_file_name, 'w') as output_file:
    output_file.writelines(converted_lines)

print(f"Converted file saved as '{output_file_name}'")
