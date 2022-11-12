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

class Kart:
  """
  Clase que contiene la lista de bienes para comprar
  """
  
  def __init__(self) -> None:
      self.listadecompra = []
      self.total = 0
  def addCompra(self, good:str, cantidad:int) -> bool:
    for category in Category.Categories:
      for seller in category.sellers:
        for product in seller.products:
          if product.name.lower() == good.lower():
            for i in range(cantidad):
              self.listadecompra.append(product)
            total = product.price*cantidad
            print(f"Se ha agregado {cantidad} unidades de {product.name} al carrito")
            time.sleep(0.3)
            print(f"Por un valor de {total}")
            self.total += total
            time.sleep(0.3)
            print(f"El total de compra es de {self.total}")
            return True
    print(f"No se ha encontrado el producto: -{good}-")
    print("Por favor trate de nuevo o use el catalogo")
    return False
  
  def removerCompra(self, good:str) -> bool:
    self.listadecompra = [value for value in self.listadecompra if value.name.lower() != good.lower()]
   
Kart.Carrito = Kart()

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
      if len(Kart.Carrito.listadecompra) > 0:
        respuesta = input(f"Esta seguro que quiere cerrar el programa?\nSu carrito contiene {len(Kart.Carrito.listadecompra)} item por un total de {Kart.Carrito.total}\n")
        time.sleep(0.3)
        if(respuesta.lower()!= "si"):
          print("No se cerrara el programa. Continue")
          return
        
      print("La aplicacion se cerrara pronto. Gracias por hacer uso de esta")
      time.sleep(1)
      print("\nAtte. Daniel Morillo y Mateo Suarez")
      time.sleep(2)
      Command.continuar = False
      #Command.continuar = False
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
              print(f"\t- {prod.name}:\t{prod.price}")
            time.sleep(1)
            print("\n\t El vendedor se encuentra en", sel.location)
    elif command[0] == "shop":
      if len(command) == 1:
        print("Se mostraran los contenidos actuales de su carrito de compra")
        time.sleep(1)
        print(" ")
        if len(Kart.Carrito.listadecompra) == 0:
          print("El carrito se encuentra vacio en el momento")
          print("Use el comando shop + nombre del producto + cantidad de producto")
        else:
          print("\tPrecio \tProducto\n")
          for products in Kart.Carrito.listadecompra:
            time.sleep(0.3)
            print(f"\t{products.price}\t{products.name}")
          time.sleep(0.4)
          print(f"\nEl total de compra es de {Kart.Carrito.total}")
      elif len(command) == 2:
        Kart.Carrito.addCompra(command[1], int(input(
          "\tNo confirmo una cantidad de producto\n\tQue cantidad desearia?\n"
        )))
      else:
        if command[2] == "0":
          Kart.Carrito.removeCompra(command[1])
        else:
          Kart.Carrito.addCompra(command[1], int(command[2]))

    elif command[0] == "checkout":
      print("prepare to buy list of products in cart")
      print("Not Implemented")
    elif command[0] == "cashin":
      print("manage account credit and payment methods")
      print("Not Implemented")
    else:
      print("Comando invalido, trate de nuevo")