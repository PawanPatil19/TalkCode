import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak What You Want To Code :")
    audio = r.listen(source)
    try:
        is_string = False
        is_print = False
        is_integer = False
        initializer = False
        cnt_variable = 1
        reached_next = False
        txt = ""
        is_add=True

        f = open("code.txt", "w")
        text = r.recognize_google(audio)
        for x in text.split():
            print(x)
            if x == "start":
                start_sequence = "#include <iostream>\nusing namespace std;\nint main()\n{\n"
                f.write(start_sequence)
            elif x == "print":
                is_print = True
                print_sequence = "cout << "
                f.write(print_sequence)

            elif x == "initialize" or x == "initialise":
                initializer = True

            elif x == "string":
                is_string = True
                if (initializer):
                    f.write("string var" + str(cnt_variable) + " = ")
                    cnt_variable += 1


            elif x=="add":
                continue



            elif x == "integer":
                is_integer = True
                if (initializer):
                    f.write("int var" + str(cnt_variable) + " = ")
                    cnt_variable += 1

            elif x == "with":
                continue

            elif x == "next":
                if (is_string):
                    f.write('"' + txt + '"')
                elif (is_integer):
                    f.write(txt)
                txt = ""
                is_string = False
                is_integer = False
                initializer = False

                f.write(";\n")

            else:
                if (is_string):
                    if reached_next:
                        txt = ""
                    else:
                        txt = txt + " " + x

                elif (is_integer):
                    txt = x

        f.write("}")
        f.close()
    except:
        print("Sorry could not recognize what you said")
