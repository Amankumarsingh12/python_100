class Mail_for():
    def send_it(self, msg, data):
        path = f"./Mail_merge/Output/ReadyToSend/letter_for_{msg}.txt"
        with open(path, "w") as file:
            file.write(data)