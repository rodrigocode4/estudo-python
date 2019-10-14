def executar(funcao):
    if callable(funcao):
        funcao()


def bomdia():
    print("Bom dia!")


def boatarde():
    print("Boa tarde!")


if __name__ == "__main__":
    executar(bomdia)
    executar(boatarde)
    executar(1)
