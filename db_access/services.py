import json
import requests
from domain.user_class import User
from domain.product_class import Product
from decimal import Decimal

identification = False
def userAuthentication(username, password):
    user = User(username, password)
    data = user.toJSON()
    identification = True
    return identification
    #res = requests.post('http://localhost:5000/api/prediction', json=data)
    #if res.ok:
    #    authentication = res["authentication"]
    #    return authenticationres = requests.get('http://localhost:5000/api/database')
    #     res = res.json()
    #     print("res", res)
    #     productList = []
    #else:
    #    print("Service offline. Please contact your service manager")
    #    return True

def getAllProducts():
    productList = []
    res = requests.get('http://localhost:5000/api/database')
    res = res.json()
    productsRes = res["productList"]
    for productRes in productsRes:
        productName = productRes["product"]["name"]
        productPrice = float(productRes["product"]["price"])
        product = Product(productName, productPrice)
        productList.append(product)
    return productList

def editProduct(oldProduct, newProduct):
    req = {"oldproduct": {"name": oldProduct.getName(), "price": oldProduct.getPrice()},
           "newproduct": {"name": newProduct.getName(), "price": newProduct.getPrice()}}

    res = requests.post('http://localhost:5000/api/database/edit', json=req)
    res = res.json()
    productList = res["productList"]
    if productList == "Product not found":
        return False
    else:
        print(res)
        return True