class Quize:

    def __init__(self, q_list) :
        self.que_num = 0
        self.question = q_list
        self.score = 0

    def still_has_que(self):
        if self.que_num <= 10 :
            return True
        else :
            return False


    def next_que(self):
        current_que = self.question[self.que_num] 
        self.que_num += 1
        user_ans= input(f"Q.{self.que_num}: {current_que.text} (True/false)")
        self.check_ans(user_ans, current_que.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("you are right")
            self.score += 1
        else:
            print("wrong")
        
        print(f"{self.score}")
        