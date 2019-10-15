#!/usr/bin/python3

bloco_atrs = ("bloco_accesskey", "bloco_id")
ul_atrs = ("ul_id", "ul_style")


def filtrar_atrs(informados, suportados):
    return " ".join(
        f'{key.split("_")[-1]}="{value}"'
        for key, value in informados.items()
        if key in suportados
    )


def tag_bloco(conteudo, *args, classe="success", inline=False, **kwargs):
    tag = "span" if inline else "div"
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = filtrar_atrs(kwargs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_list(*items, **kwargs):
    lista = "".join((f"<li>{item}</li>" for item in items))
    return f"<ul {filtrar_atrs(kwargs, ul_atrs)}>{lista}</ul>"


if __name__ == "__main__":
    print(tag_bloco("Sucesso!!!"))
    print(tag_bloco("inline e classe", classe="info", inline=True))
    print(tag_bloco("inline", inline=True))
    print(tag_bloco("Falhou!!!", classe="error"))
    print(tag_bloco(classe="error", conteudo="Falhou!!!"))
    print(tag_bloco(conteudo=tag_list("Item 1", "Item 2", "Item 3"), classe="default"))
    print(tag_bloco(tag_list, "Sábado", "Domingo", classe="info", inline=True))

    print(
        tag_bloco(
            tag_list,
            "Item 1",
            "Item 2",
            classe="danger",
            bloco_accesskey="m",
            bloco_id="conteudo",
            ul_id="lista",
        )
    )
