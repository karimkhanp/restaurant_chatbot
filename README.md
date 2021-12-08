# restaurant_chatbot
Demo chatbot which show how NLP can be used to develop quick chatbot 

Requirements
1. NLTK
2. Stanford core nlp NER package - https://nlp.stanford.edu/software/CRF-NER.html#Download

How to run

        python restaurant_bot.py 

        How can I help you today?
        Can you help me book a table for 2 tonight at 8pm in San Francisco? 
        Entities : Location : San Francisco, Guest : 2, Time :  tonight 8pm
        Please go ahead ... : 
        Can you help me book a table for tomorrow at 6pm in Palo Alto? 
        Entities : Location : Palo Alto, Guest :  , Time :  tomorrow 6pm
        Please go ahead ... : 
        For 2 of us please 

        Entities : Location : , Guest : 2, Time :  
        Please go ahead ... : 
        Entities : Location : , Guest : None, Time : None 
        Please go ahead ... : 
        Possible to reserve French Laundry on 25th Dec at 6pm for 4 of us? 
        Entities : Location : , Guest :  , Time : 25th 6pm
        Please go ahead ... : 
