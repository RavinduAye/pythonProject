import speech_recognition as sr

r = sr.Recognizer()

with open('medicines') as f:
    medicines = f.read().splitlines()

with sr.Microphone() as source:

    import medicineSelection1

    print("Speak Anything :")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

        if text in medicines:
            text1 = text


        else:
            text2 = "Doesn't match"
            import medicineSelection2

    except:

        print("Sorry could not recognize what you said")

        import medicineSelection3
