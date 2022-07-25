# X - konwertuje tekst jako odwórcony alfabet, Y - "dekodcuje" odwrócony tekst

def x(string):

    sentence = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    return(string.translate(sentence))

def y(string):
        
    sentence = str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    return(string.translate(sentence))
 
while True:

    global users_input

    print('Wybierz funkcje: x lub y ')
    users_input = input()
    
    if users_input == "x":
        
        def st():

            print("Enter text to convert: ")

            string = input() 
            x(string)
        
               
            #new_input == string
            return string, print(x(string))

        st()


    if users_input == "y":
        
        def st2():

            print("Enter text to convert: ")

            string = input() 
            x(string)
        
               
            #new_input == string
            return string, print(y(string))

        st2()
