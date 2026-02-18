import random

words = words = [ "profe braulio", "salma", "software", "valentines", "sanguijuela", "graduacion", "computadora", "abrigo", "desarrollar",
          "otorrinolaringologo", "new horizons", "development", "successful", "arancel", "abracadabrante"
]
game_words = random.sample (words, 15)
mistakes = 0 
total = len(game_words)
count = 1 

print("Escribe la siguiente palabra y presiona Enter")

for word in game_words:
    print("palabra", count, "de", total, ":", word)
    user = input("tu respuesta: ").strip()

    if user.lower() == "exit":
        print("juego terminado")
        break

    if user == word:
        print("Correcto!")
    else:
        print("Incorrecto!")
        mistakes += 1

    print("Intentos fallidos:", mistakes)
    print()
    count += 1

played = count - 1

if played > 0:
    correct = played - mistakes
    accuracy = (correct / played) * 100

    print("juego terminado")
    print("correctas:", correct)
    print("incorrectas:", mistakes)
    print("precisión:", round(accuracy, 2), "%")
else:
    print("No completaste ninguna palabra.")
