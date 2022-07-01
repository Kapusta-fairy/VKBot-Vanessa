from constants import *

# 'команда, которую понимает ванесса': 'её ответ'
# то, что не сокрыто в скобочки находится в constants
text_commands = {
    'капуста': 'эхб',
    'тулик': anec,
    'змий': 'гений',
    'матвей': 'мегахарош',
    'картошка': 'хороший чел, качественный',
    'влад': 'капустный стратег😎',
    'кейт': 'скажите "сус"',
    'айко': 'ЕНОТЬЯ СИЛА',
    'амогус': 'тутуту',
    'ыыы': 'ыыы',
}

gifs_commands = {
    'жидкость': gif_hedgehog,
    'рекрут сус': gif_recruit_sus,
    'картошка сус': gif_potato_sus,
    'сус': gif_sus,
    'холод': gif_cold,
    'чопалах': gif_chop,
}

indirect_gifs_command = {
    'браво': gif_bravo,
    'бесплатн': gif_free,
    'платн': gif_pay,
    'зарплат': gif_salary,
    'модест': gif_modest,
    'вика': gif_bad,
    'вику': gif_bad,
    'викочк': gif_bad,
}

img_commands = {
    'кринж': img_kringe,
    'резня': img_carnage,
}

indirect_img_commands = {
    'зомби в топе': img_zombi,
}

stick_commands = {
    'лич': stick_clown,
}

# эти команды имеют сложный ответ, который вызывается в main
helpful_commands = [
    'фракция',       # 0
    'д',             # 1
    'навык',         # 2
    'абоба',         # 3
]