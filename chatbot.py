from chatterbot import chatbot
from chatterbot.trainers import listTrainer 
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot ChatBot (names "PyBot", read only-True, logic adapters=
['chatterbot.logic.Mathematical Evaluation',
'chatterbot.logic.bestmatch']
)
small_talk ['hi there', 'bla bla bla',
'how do you do?',
'how are you?',
i\ 'm cool', 'i\m ok',
'glad to hear that',
'i\m fine',
'sorry to hear that',
'whats your name?',
i\'m PyBot. Ask me any math question, please?'
]
talk 1= ['Best Instagram Page',
'Everyone is coding'
] List trainer listTrainer(my_bot)
for item in (small_talk, talk 1): list trainer.train(item)
corpus trainer ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterBot.corpus.English')
print(my_bot,getresponse('bla blabla blka'))
print(my_bot.getresponse('I feel you awesome toda.'))
print(my_bot.getresponse("Whats your name"))