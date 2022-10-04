from typing import List, Set, Dict, Tuple, Optional

class Product:
  def __init__(self, name:str, price:int) -> None:
    self.name = name
    self.price = price

class Seller:
  Sellers = []
  def __init__(self, name:str, location:str, products:List[Product]) -> None:
    self.name = name
    self.products = products
    self.location = location
    Seller.Sellers.append(self)

class Category:
  Categories = []
  def __init__(self, name:str, sellers:List[Seller]) -> None:
    self.name = name
    self.sellers = sellers
    Category.Categories.append(self)

class Command:
  continuar = True
  Comandos = []
  def __init__(self, name:str, help:str) -> None:
    self.name = name
    self.help = help
    Command.Comandos.append(self)

  def metodo(command):
    if command[0] == "exit":
      print("La aplicacion se cerrara pronto. Gracias por hacer uso de esta")
      print("Atte. Daniel Morillo y Mateo Suarez")
      Command.continuar = False
    elif command[0] == "project":
      print("Este proyecto es realizado para la clase OOP")
    elif command[0] == "catalog":
      if len(command) == 1 or command[1] == "":
        for cat in Category.Categories:
          print("\t", cat.name)
      else:
        for cat in Category.Categories:
          if cat.name.lower() == command[1].lower():
            for seller in cat.sellers:
              print("\t", seller.name)
        for sel in Seller.Sellers:
          if sel.name.lower() == command[1].lower():
            for prod in sel.products:
              print("\t", prod.name, "\t", prod.price)
            print("\t El vendedor se encuentra en", sel.location)
    else:
      print("Comando invalido, trate de nuevo")