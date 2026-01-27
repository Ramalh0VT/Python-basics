def test():
    while True:
        password_guess = input("What do you think the password is?\n")

        if password_guess == "PROTOCOLO":
            print("You guessed the password right!")
            break

        else:
            print("Os lobos vão começar a rosnar de um jeito nunca antes visto")
    
while True:
    test()
    while True:
        advinhacao = input("Se você não acertar a palavra algo terrível vai acontecer.")

        if advinhacao == "LAPRIFA":
            print("S realizações ju! Parabéns! Que seu dia seja!")
            break

        else:
            print("Já era.")
