import csv


def prato_mas_pedido_maria(orders):
    count_order = {}
    maria_mais_vendidos = [
        order["order"] for order in orders if order["client"] == "maria"
    ]

    for v in maria_mais_vendidos:
        if v in count_order:
            count_order[v] += 1
        else:
            count_order[v] = 1

    return max(count_order, key=count_order.get)


def vezes_arnaldo_pediu_hamburguer(orders):
    count = 0
    orders_arnaldo = [
        order["order"] for order in orders if order["client"] == "arnaldo"
    ]

    for v in orders_arnaldo:
        if v == "hamburguer":
            count += 1
    return count


def joao_não_pediu(menu, orders):
    lista_joao = set()

    for v in orders:
        if v["client"] == "joao":
            lista_joao.add(v["order"])

    return menu.difference(lista_joao)


def dias_joao_naofoi_lanchonete(orders, days):
    list_joao = set()

    for v in orders:
        if v["client"] == "joao":
            list_joao.add(v["day"])
    return days.difference(list_joao)


def analyze_log(path_to_file):
    restaurante = []
    menu = set()
    days_complete = set()

    try:
        with open(path_to_file, "r") as file:
            file_reader = csv.reader(file)
            for client, order, day in file_reader:
                restaurante.append(
                    {"client": client, "order": order, "day": day}
                )
                menu.add(order)
                days_complete.add(day)
    except FileNotFoundError:
        if not path_to_file.endswith(".csv"):
            raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    pedidos_maria = prato_mas_pedido_maria(restaurante)
    arnaldo_pedidos = vezes_arnaldo_pediu_hamburguer(restaurante)
    joao = {
        "nao_ordenou": joao_não_pediu(menu, restaurante),
        "nao_visitou": dias_joao_naofoi_lanchonete(restaurante, days_complete),
    }

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{pedidos_maria}\n"
            f"{arnaldo_pedidos}\n"
            f"{joao['nao_ordenou']}\n"
            f"{joao['nao_visitou']}\n"
        )
