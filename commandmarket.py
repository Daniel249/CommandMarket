from typing import List, Set, Dict, Tuple, Optional
import time

class Product:
  """
  Clase de producto con su nombre y precio para realizar la compra
  """
  def __init__(self, name:str, price:int) -> None:
    self.name = name
    self.price = price

class Seller:
  """
  Clase vendedor para navegacion por nombre y contener todos los productos
  """
  Sellers = []
  def __init__(self, name:str, location:str, products:List[Product]) -> None:
    self.name = name
    self.products = products
    self.location = location
    Seller.Sellers.append(self)

class Category:
  """
  Clase de categorias de productos para navegacion
  """
  Categories = []
  def __init__(self, name:str, sellers:List[Seller]) -> None:
    self.name = name
    self.sellers = sellers
    Category.Categories.append(self)

class Command:
  """
  Clase que contiene la lista de comandos y sus funciones
  """
  continuar = True
  def __init__(self, name:str, help:str) -> None:
    self.name = name
    self.help = help

  def metodo(command:List[str]):
    if command[0] == "exit":
      print("La aplicacion se cerrara pronto. Gracias por hacer uso de esta")
      print("\nAtte. Daniel Morillo y Mateo Suarez")
      time.sleep(3)

      Command.continuar = False
    elif command[0] == "project":
      print("Este proyecto es realizado para la clase OOP de Jose D. Posada")
      print("Realizado por Daniel Morillo y Mateo Suarez")
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
    elif command[0] == "shop":
      print("add products to buying cart")
      print("Not Implemented")
    elif command[0] == "checkout":
      print("prepare to buy list of products in cart")
      print("Not Implemented")
    elif command[0] == "cashin":
      print("manage account credit and payment methods")
      print("Not Implemented")
    else:
      print("Comando invalido, trate de nuevo")