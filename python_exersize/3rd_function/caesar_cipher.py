alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("type 'encoder' to encrypt, type 'decoder' to decrypt: ")


def encoder(text,shift):
    encoded = ""
    for i in text:
        pos = alpha.index(i)
        encoded += alpha[pos+shift]
    print(encoded)
    

def decoder(text,shift):
    decoded = ""
    for i in text :
        pos = alpha.index(i)
        decoded += alpha[pos-shift]
    print(decoded)


if direction == "encoder":
    text = input("type your message:\n").lower()
    shift = int(input("type your shift number: "))
    encoder(text,shift)
elif direction == "decoder":
    text = input("type your message:\n").lower()
    shift = int(input("type your shift number: "))
    decoder(text,shift)
else:
    print("enter a Right word")








'''encoder_list=[]

shift_nu=1
for i in range(0,(26-shift_nu)):
    encoder_list += alpha[i+shift_nu]

for i in range(0,shift_nu):
    encoder_list += alpha[i]

print(encoder_list)'''