current_language = "it_IT" # se eu trocar o resultado vai ser diferente --> "it_IT"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)