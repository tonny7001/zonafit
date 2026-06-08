# uso de una funcion normal


def sumar(a, b, c):
    return a + b + c


print(sumar(10, 20, 25))

sumar_con_lambda = lambda a, b, c: a + b + c
print(
    sumar_con_lambda(
        10,
        25,
        36,
    )
)
