from question_model import Question
from quiz_data import question_data

from quize import Quize

ques_bank = []

for que in question_data :
    que_text = que["text"]
    que_ans = que["answer"]

    new_question = Question(que_text,que_ans)
    ques_bank.append(new_question)

quize = Quize(ques_bank)
while(Quize.still_has_que(quize)):
    quize.next_que()
    
