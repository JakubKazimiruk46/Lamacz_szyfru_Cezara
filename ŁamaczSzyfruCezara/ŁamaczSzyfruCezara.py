def main():

    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        UserText = input("Podaj tekst: ").upper()


        TranslatedText = ''
        Key = 1

        while Key <= 25:
            for x in UserText:
                if x in Alphabet:
                
                    num = Alphabet.find(x)
                    num = num - Key

                    if num >= 26:
                        num = num - len(Alphabet)
                    elif num < 0:
                        num = num + len(Alphabet)

                    TranslatedText += Alphabet[num]
            
                else:
                    TranslatedText += x
                
            
         
            print(f'#{Key} {TranslatedText}')
            print()
            Key += 1
            TranslatedText = ''

main()
