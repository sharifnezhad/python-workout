import os
def add_new_words(word_list):
    while True:
        en_word=input('english word: ')
        found = False
        for i in word_list:
            if i['en']==en_word:
                found=True
        if found==False:
            pr_word = input('persian word: ')
            word_list.append({'en':en_word,'pr':pr_word})
            if input('Do you want to add a new word? (y/n)')=='n':
                break
        else:
            print('This word is in the dictionary')
def save_words(word_list):
    my_file = open('database.txt', 'w')
    for i in range(len(word_list)):
        if i != len(word_list) - 1:
            my_file.write(
                str(word_list[i]['en']) + ',' + word_list[i]['pr'] + '\n')
        else:
            my_file.write(
                str(word_list[i]['en']) + ',' + word_list[i]['pr'])
    my_file.close()
    exit()
def translate_en(word_list):
    sentence=input('Enter the desired sentence?\n')
    verb=[]
    if '. ' in sentence:
        sentence=sentence.split('.')
    verb.append(sentence.split(' '))
    word_str=[]
    str_words=' '
    for i in range(len(verb)):
        for k in range(len(verb[i])):
            for j in word_list:
                if verb[i][k]==j['en']:
                    word_str.append(j['pr'])
                    break
                elif verb[i][k]==verb[i][k].capitalize():
                    word_str.append(verb[i][k])
                    break
        word_str.append('.')
    print(str_words.join(word_str))
def translate_pr(word_list):
    sentence = input('Enter the desired sentence?\n')
    verb = []
    if '. ' in sentence:
        sentence = sentence.split('.')
    verb.append(sentence.split(' '))
    word_str = []
    str_words = ' '
    for i in range(len(verb)):
        for k in range(len(verb[i])):
            for j in word_list:
                if verb[i][k] == j['pr']:
                    word_str.append(j['en'])
                    break
                elif verb[i][k] == verb[i][k].capitalize():
                    word_str.append(verb[i][k])
                    break
        word_str.append('.')
    print(str_words.join(word_str))
def find_file(file_name,path):
    for root, dirs, files in os.walk(path):
        if file_name in files:
            return os.path.join(root, file_name)
    return False


try:
    myfile=open('database.txt','r')
except:
    print('file not find ://')
    exit()
words=myfile.read()
myfile.close()
words_list=words.split('\n')
WORDS=[]
for i in range(len(words_list)):
    word=words_list[i].split(',')
    mydic={}
    WORDS.append({'en':word[0],'pr':word[1]})
while True:
    print('1. add a new words\n'
              '2. translation english-->persian\n'
              '3. translation persian--> english\n'
              '4. exit\n')
    number_munu=int(input('enter a number: '))
    if number_munu==1:
        add_new_words(WORDS)
    elif number_munu==2:
        translate_en(WORDS)
    elif number_munu==3:
        translate_pr(WORDS)
    elif number_munu==4:
        save_words(WORDS)

