from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/home")
def home():
    return 'hello world'


class Product:
    def __init__(self, id, name, desc, img_url, category, price):
        self.__id = id
        self.__name = name
        self.__desc = desc
        self.__img_url = img_url
        self.__price = price
        self.__category = category

    def prod_dict(self):
        return {
             "id": self.__id,
            "name": self.__name,
            "desc": self.__desc,
            "img_url": self.__img_url,
            "price": self.__price,
            "category": self.__category,
        }
    

    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, desc):
        self.__desc = desc
    @property
    def img_url(self):
        return self.__img_url
    @img_url.setter
    def img_url(self, img_url):
        self.__img_url = img_url
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category):
        self.__category = category

product_first_id = 0
products = []
@app.route("/products", methods=['GET'])
def AllProducts():
    all_products =[]
    for product in products:
        all_products.append(product.prod_dict())
    return jsonify(all_products)


@app.route("/products/<int:product_id>", methods=['PUT'])
def UpdateProduct(product_id):
    if request.method == 'PUT':
        product = next((p for p in products if p.id == product_id), None)
        if product == None:
            return "Product not found 404"

        data = request.get_json()

        name = data["name"]
        desc = data["desc"]
        img_url = data["img_url"]
        price = data["price"]
        category = data["category"]

        product.name = name
        product.desc = desc
        product.img_url = img_url
        product.price = price
        product.category = category

    return jsonify(product.prod_dict())


@app.route("/create", methods=['POST'])
def AddProduct():
    global product_first_id
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        desc = data["desc"]
        img_url = data["img_url"]
        price = data["price"]
        category = data["category"]
        product = Product(
            id=product_first_id,
            name=name,
            desc=desc,
            img_url=img_url,
            price=price,
            category=category

        )
        products.append(product)
        product_first_id += 1

    return jsonify(product.prod_dict())

@app.route("/products/<int:product_id>", methods=["DELETE"])
def DeleteItem(product_id):
    if request.method == "DELETE":
        product = next((e for e in products if e.id == product_id), None)
        if product == "None":
            return "Product Not Found 404"
        products.remove(product)
    return "Data Deleted Successfully"




if __name__ == '__main__':
    app.run(debug=True, port=5820)