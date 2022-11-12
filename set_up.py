from commandmarket import Command, Product, Category, Seller
from typing import List

def initialize() -> List[Command]:
    print("Initializing...")
    project = Command("project", "short description of project conception")
    catalog = Command("catalog", "show and browse types of products")
    shop = Command("shop", "add products to buying cart")
    checkout = Command("checkout", "prepare to buy list of products in cart")
    cashin = Command("cashin", "manage account credit and payment methods")
    exit = Command("exit", "close application")
    comandos = [project, catalog, shop, checkout, cashin, exit]

    dulce1 = Product("- Burbujet: ", 900)
    dulce2 = Product("- Barrilete: ", 1000)
    dulce3 = Product("- Galleta festival: ", 500)
    dulce4 = Product("- Chocorramo: ", 4000)
    dulce5 = Product("- ChocoBreak: ", 200)
    dulce6 = Product("- Bom Bom Bum: ", 500)
    dulce7 = Product("- Gansito: ", 1000)
    dulce8 = Product("- Trululu: ", 200)
    dulce9 = Product("- Chocolatina jet: ", 300)
    dulce10 = Product("- Choclitos: ", 700)
    dulce11 = Product("- Galleta Muu: ", 300)
    dulce12 = Product("- Quipitos: ", 500)
    dulce13 = Product("- Chicles: ", 200)
    dulce14 = Product("- Trocipollo: ", 600)

    vendedordulces1 = Seller("DulcesMau", "Bloque D", [dulce1, dulce2, dulce3, dulce4, 
    dulce5, dulce6, dulce7, dulce8, dulce9])
    vendedordulces2 = Seller("DulSamir", "Detras del coliseo", [dulce1, dulce6, dulce8, dulce9, dulce13, dulce14])
    vendedordulces3 = Seller("FerDulces", "Bloque J", [dulce2, dulce4, dulce6, dulce8, dulce10, dulce12, dulce14, dulce1, dulce3])
    categoriadulces = Category("Dulces", [vendedordulces1, vendedordulces2, vendedordulces3])

    postre1 = Product("- Postre Napoleon: ", 5000)
    postre2 = Product("- Postre tres leches: ", 5000)
    postre3 = Product("- Postre de quesillo", 4000)
    postre4 = Product("- Postre de oreo: ", 6000)
    postre5 = Product("- Postre de milo: ", 6000)
    postre6 = Product("- Postre de chocolate: ", 7000)
    postre7 = Product("- Postre de vainilla: ", 6500)
    postre8 = Product("- Postre de arequipes: ", 5000)
    postre9 = Product("- Postre de maracuya: ", 3500)

    vendedorpostre1 = Seller("PostresAriana", "Bloque K", [postre1, postre2, postre3, postre4, 
    postre5])
    vendedorpostre2 = Seller("CamiPostres", "Bloque G", [postre6, postre7, postre8, postre9])
    vendedorpostre3 = Seller("PostresJulio", "Bloque M", [postre2, postre4, postre6, postre8])
    categoriapostre = Category("Postres", [vendedorpostre1, vendedorpostre2, vendedorpostre3])

    articulo1 = Product("- Gorras Nike: ", 20000)
    articulo2 = Product("- Gorras Adidas: ", 20000)
    articulo3 = Product("- Air Force 1: ", 150000)
    articulo4 = Product("- Jordan retro: ", 250000)
    articulo5 = Product("- Camiseta Oversize Nike: ", 25000)
    articulo6 = Product("- Camisa local del Barcelona: ", 140000)
    articulo7 = Product("- Medias Nike: ", 12000)
    articulo8 = Product("- Medias Adidas: ", 12000)
    articulo9 = Product("- Blue Jeans Strech ", 80000)
    
    vendedorropa1 = Seller("VestuarioUninorte", "LasPalmeras", [articulo1, articulo2, articulo3, articulo4])
    vendedorropa2 = Seller("JankyStyles", "Bloque M", [articulo4, articulo5, articulo6, articulo7])
    vendedorropa3 = Seller("Pedro Marks", "Bambu 3", [articulo6, articulo7, articulo8, articulo9])
    categoriaropa = Category("Ropa", [vendedorropa1, vendedorropa2, vendedorropa3])

    print("Done!")
    return comandos