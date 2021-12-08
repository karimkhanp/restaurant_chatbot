from ner import RestoBot
from timex import NltkTimex

class RestaurantChatbot(object):
    def __init__(self):
        pass

    def init_chat(self):        
        print("How can I help you today?")
        while True:
            query = input()
            time = NltkTimex().tag(query)
            location = RestoBot().NERTagger(query)
            guest = RestoBot().getGuest(query)
            date = RestoBot().getDate(query)
            #return = { "result": "res", "flag" : 1}
	    #imp_entities
            print("Entities : " + "Location : " + ' '.join(location) + ', Guest : ' + str(guest) + ", Time : " + str(date) + ' ' + str(' '.join(time)))
            print("Please go ahead ... : ")
            

if __name__ == '__main__':
    RestaurantChatbot().init_chat()
