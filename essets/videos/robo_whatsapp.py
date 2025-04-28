import pywhatkit as kit

# Enviar uma mensagem para o seu número de WhatsApp
# Formato do número: "+55" para Brasil, seguido do número
# Seu número é: +55 62 98160 5863
kit.sendwhatmsg("+55 62981605863", "Olá, Mundo!", 15, 30)  # Envia a mensagem às 15:30
