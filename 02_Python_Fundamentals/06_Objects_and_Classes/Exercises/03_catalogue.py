class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name:str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter:str):
        sorted_products = [product for product in self.products if product[0] == first_letter]
        return sorted_products

    def __repr__(self):
        self.products.sort()
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(self.products)
        return result
