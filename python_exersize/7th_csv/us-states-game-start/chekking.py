import pandas

class check():

    def __init__(self) :
        pass

    def check_ans(self, ans):
        import pandas
        self.data = pandas.read_csv("50_states.csv")
        self.data = self.data[self.data["state"] == ans]
        if not (self.data.empty) :
            self.x_cor = self.data['x'].values[0]
            self.y_cor = self.data['y'].values[0]
            return [self.x_cor, self.y_cor]
    