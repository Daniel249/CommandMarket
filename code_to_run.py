from set_up import initialize
from commandmarket import Command
import time

comandos = initialize()
print("------------------ Bienvenido ------------------")
print("Se encuentra en la terminal amarilla de uninorte")
print("-----Si necesita ayuda use el comando help-----\n")
while Command.continuar:
  command = input().split(" ")
  time.sleep(1)
  if command[0] == "help":
    if len(command) == 1 or command[1] == "":
      time.sleep(0.3)
      print("Los comandos son los siguientes:")
      for com in comandos:
        time.sleep(0.2)
        print("\t", com.name)
    else:
      for com in comandos:
        if com.name == command[1]:
          print(com.name + ": " + com.help)
  else:
    Command.metodo(command)