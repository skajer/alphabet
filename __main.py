# X - converts alphabet backwards, Y - "decodes" X function

def x(string):

    sentence = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    return(string.translate(sentence))

def y(string):
        
    sentence = str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz')
    return(string.translate(sentence))
 
while True:

    global users_input

    print('Choose function: x or y ')
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


### 😎