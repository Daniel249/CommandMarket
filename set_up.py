from commandmarket import Command, Product, Category, Seller
from typing import List

def initialize() -> List[Command]:
    print("Initializing...")
    project = Command("project", "short description of project conception")
    catalog = Command("catalog", "show and browse types of products")
    shop = Command("shop", "add product to cart")
    checkout = Command("checkout", "prepare to buy list of products in cart")
    cashin = Command("cashin", "manage account credit and payment methods")
    exit = Command("exit", "close application")
    comandos = [project, catalog, shop, checkout, cashin, exit]

    dulce1 = Product("Burbujet", 900)
    dulce2 = Product("Barrilete", 1000)
    dulce3 = Product("Brownie", 2000)
    articulo1 = Product("Gorra", 15000)
    articulo2 = Product("Camiseta", 20000)
    vendedordulces1 = Seller("DulcesMau", "BloqueD", [dulce1, dulce2, dulce3])
    vendedorropa1 = Seller("VestuarioUninorte", "LasPalmeras", [articulo1, articulo2])
    categoriadulces = Category("Dulces", [vendedordulces1])
    categoriaropa = Category("Ropa", [vendedorropa1])
    print("Done!")
    return comandos