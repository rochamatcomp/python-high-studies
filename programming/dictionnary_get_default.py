class Products(OrderedEnum):
    SOY_BRAN = "Farelo"
    SUGAR = "Açúcar"
    SOY = "Soja"
    CORN = "Milho"
    COPPER = "Cobre"
    PIG_IRON = "Ferro Gusa"
    MANGANESE = "Manganês"

capacities = {
    Products.CORN: 5000,
    Products.SOY: 5000
}

total = sum(
    capacities[product]
    for product in Products
)

total = sum(
    capacities.get(key=product, default=0)
    for product in Products
)