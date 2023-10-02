#Ayaan Bajwa 
#Student ID: 100864399
#Lab 6 Top 1o Words


from collections import Counter
import string

class WordCounter():
    def __init__(self, words_dict):
        self.words_dict = words_dict
        
    def get_words_dict(self):
        return self.words_dict  
    
    def top_10_words(self):
        top10 = self.words_dict.most_common(10)
        print(top10)
        
    
def main_file_open():
        
    with open("text.txt", "r") as file:
        txt=file.read()
        change =str.maketrans("", "", string.punctuation)
        txt=txt.translate(change)
        listText = txt.split()
        filecnt=Counter(listText)
        return filecnt
            

if __name__ =="__main__":
    
    dict = main_file_open()
    words_counter = WordCounter(dict)
    print(words_counter.get_words_dict()) #print all the disctionar
    words_counter.top_10_words() #print(top ten word)

