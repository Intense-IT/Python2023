import json


with open('lesson14/text.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write('Просто текст')

student_score = {
    'Magomed': 10,
    'Мурад': 12
}
with open('lesson14/studs.json', 'w', encoding='UTF-8') as json_file:
    json.dump(student_score, json_file, ensure_ascii=False, indent=2)