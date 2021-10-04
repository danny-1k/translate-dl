import os
import gtts
from tqdm import tqdm
import argparse
import codecs

parser = argparse.ArgumentParser()

parser.add_argument('--words',default='words.txt')
parser.add_argument('--lang',default='fr')

args = parser.parse_args()

wordf = args.words
lang = args.lang

if 'mp3' not in os.listdir():
    print('Creating mp3 folder ...')
    os.mkdir('mp3')


try:
    with codecs.open(wordf,encoding='latin1') as f:
        for word in tqdm(f.readlines()):
            word = word.replace('\n','').replace('\r','')
            tts = gtts.gTTS(word,lang=lang)
            safe_file_name = ''.join(['_' if i in '<>:"/\\|?* ' else i for i in word])
            safe_file_name = os.path.join('mp3',safe_file_name+'.mp3')
            tts.save(safe_file_name)

except FileNotFoundError:
    print(f'File not found : {wordf}')