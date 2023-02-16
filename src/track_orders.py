class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self) -> None:
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append(
            {"client": customer, "dish": order, "day": day}
        )

    def get_most_ordered_dish_per_customer(self, customer):
        lista = []
        for order in self.orders:
            if order["client"] == customer:
                lista.append(order["dish"])
        return max(lista, key=lista.count)

    def get_never_ordered_per_customer(self, customer):
        ordered = set()
        customer_ordered = set()
        for order in self.orders:
            if order["client"] == customer:
                customer_ordered.add(order["dish"])
            ordered.add(order["dish"])
        return ordered.difference(customer_ordered)

    def get_days_never_visited_per_customer(self, customer):
        dias = set()
        customer_dias = set()
        for order in self.orders:
            if order["client"] == customer:
                customer_dias.add(order["day"])
            dias.add(order["day"])
        return dias.difference(customer_dias)

    def get_busiest_day(self):
        count = {}
        movimento = self.orders[0]["day"]

        for order in self.orders:

            if order["day"] in count:
                count[order["day"]] += 1
            else:
                count[order["day"]] = 1
            if count[order["day"]] > count[movimento]:
                movimento = order["day"]
        return movimento

    def get_least_busy_day(self):
        count = {}

        for order in self.orders:
            poco_movimento = order["day"]
            if order["day"] in count:
                count[order["day"]] += 1
            else:
                count[order["day"]] = 1
            if count[order["day"]] < count[poco_movimento]:
                poco_movimento = order["day"]
        return poco_movimento
