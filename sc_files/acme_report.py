"""A module for printing a report of randomly-generated products."""

from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Generates random product names to add to the product list."""

    products = []

    for i in range(num_products):
        name = ''
        price = randint(5, 100)
        weight = randint(5, 100)
        flamm = uniform(0.0, 2.5)

        shuffled_adj = sample(ADJECTIVES, k=5)
        rand_index = randint(0, len(ADJECTIVES) - 1)
        rand_adj = shuffled_adj[rand_index]
        name += rand_adj

        shuffleed_nouns = sample(NOUNS, k=5)
        rand_index = randint(0, len(NOUNS) - 1)
        rand_noun = shuffleed_nouns[rand_index]
        name += ' ' + rand_noun

        product = Product(name, price=price, weight=weight, flammability=flamm)
        products.append(product)

    return products


def inventory_report(products):
    """Prints a formatted report of the generated product info."""

    report_header = """
    Acme INC. Product Report
    """
    product_header = ''
    names = []
    unique_names = 0
    sum_price = 0
    avg_price = 0
    sum_weight = 0
    avg_weight = 0
    sum_flamm = 0.0
    avg_flamm = 0.0

    print(report_header)

    for product in products:
        if product.name not in names:
            names.append(product.name)

        sum_price += product.price
        sum_weight += product.weight
        sum_flamm += product.flammability

    unique_names = len(names)
    avg_price = round(sum_price / len(products), 2)
    avg_weight = round(sum_weight / len(products), 2)
    avg_flamm = round(sum_flamm / len(products), 2)

    print(f"""
    Unique product names: {unique_names}
    Average price: ${avg_price}
    Average weight: {avg_weight} LBS
    Average flammability: {avg_flamm}
    """)

    for product in products:
        product_header = f"{product.name}: ${product.price}"

        print(f"""{product_header}
        Product ID: {product.id}
        Weight: {product.weight} LBS
        Flammability: {round(product.flammability, 2)}
        """)


if __name__ == '__main__':
    inventory_report(generate_products())
