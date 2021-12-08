# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import re

numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
          eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
          eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
          ninety|hundred|thousand|[0-9]+)"

class RestoBot(object):
    def __init__(self):
        pass

    '''
        For date parsing we can consdier Stanford date and time parser. But for quick example I am using this basic extraction
    '''
    def getDate(self, text):
        res = re.findall(numbers, text)
        date = ''
        for val in res:
            if val+'th' in text:
                return val+'th'
            elif val+'nd' in text:
                return val+'nd'
            elif val+'st' in text:
                return val+'st'
            else:
                return ''
    
    '''
        I have considered this two case for gues, based on in which other format user talks about numbers of guest, we can add more cases
    '''
    def getGuest(self, text):
        res = re.findall(numbers, text)
        guest = ''
        for val in res:
            if val + ' of' in text or 'for ' + val in text:
                return val
            else:
                return ' '
    '''
        Stanford model can be trained with our own query data. That can improve the accuracy
    '''
    def NERTagger(self, text):  
        st = StanfordNERTagger('/Users/karim/Documents/software/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz',
                               '/Users/karim/Documents/software/stanford-ner-2020-11-17/stanford-ner.jar',
                               encoding='utf-8')
           
        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)
        all_location = []
        for val in classified_text:
            if list(val)[1] == 'LOCATION':
                all_location.append(list(val)[0])

        return all_location

if __name__ == '__main__':
    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal. Lets meet on wednesday at 9am.'
    result = RestoBot().NERTagger(raw_input())
    print(result)
