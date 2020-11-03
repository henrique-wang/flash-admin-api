from db_access.services import getAllProducts
def main():
    for product in getAllProducts():
        print(product)
main()