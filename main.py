import re
import tkinter as tk
import subprocess
import urllib.request
from inscriptis import get_text

# url = input("Enter URL\n")
url = "https://www.quora.com/What-are-all-the-bad-words-and-their-meanings"
html = urllib.request.urlopen(url).read().decode('utf-8')

text = get_text(html)
path = r'E:\Projects\Abusive Comments Filter\zest.txt'
file = open(path, 'w')
file.write(text)
file.close()


class Filter(object):

    def __init__(self, original_string, clean_word='****'):
        bad_words_file = open('bad_words.txt', 'r')

        self.bad_words = set(line.strip('\n') for line in open('bad_words.txt'))
        self.original_string = original_string
        self.clean_word = clean_word

    def clean(self):
        exp = '(%s)' % '|'.join(self.bad_words)
        r = re.compile(exp, re.IGNORECASE)
        return r.sub(self.clean_word, self.original_string)


def read():
    root = tk.Tk()
    root.withdraw()
    path1 = r'E:\Projects\Abusive Comments Filter\zest.txt'
    fi = open(path1)
    content = fi.read()
    fi.close()
    f = Filter(content, clean_word='*********')
    word = f.clean()
    f1 = open('output.txt', 'w')
    f1.write(word)
    txt = r"E:\Projects\Abusive Comments Filter\output.txt"
    txt_path = r'C:\Program Files\Notepad++\notepad++.exe'
    subprocess.Popen("%s %s" % (txt_path, txt))


read()
