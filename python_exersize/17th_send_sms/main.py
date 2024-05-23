import vonage

client = vonage.Client(key="c17ebe3f", secret="TwKU0uNDXyfrIC0p")
sms = vonage.Sms(client)


def sendSms():
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "917319632498",
            "text": " hey there",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


sendSms()
