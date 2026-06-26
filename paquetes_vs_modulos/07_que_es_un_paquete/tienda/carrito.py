from tienda import productos


def total(nombres):
    return sum(productos.precio(n) for n in nombres)
