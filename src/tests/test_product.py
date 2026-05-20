from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Test Product', 'Test Brand', 9.99)
    dao.insert(product)

    product_list = dao.select_all()
    names = [p[1] for p in product_list]

    assert product.name in names

    # cleanup
    inserted_product = next(p for p in product_list if p[1] == product.name)
    dao.delete(inserted_product[0])

def test_product_update():
    product = Product(None, 'Test Product', 'Test Brand', 9.99)
    dao.insert(product)

    product_list = dao.select_all()
    inserted_product = next(p for p in product_list if p[1] == product.name)

    corrected_price = 19.99
    updated_product = Product(inserted_product[0], inserted_product[1], inserted_product[2], corrected_price)
    dao.update(updated_product)

    new_product_list = dao.select_all()
    prices = [p[3] for p in new_product_list]
    assert corrected_price in prices

    # cleanup
    dao.delete(inserted_product[0])

def test_product_delete():
    product = Product(None, 'Test Product', 'Test Brand', 9.99)
    dao.insert(product)

    product_list = dao.select_all()
    inserted_product = next(p for p in product_list if p[1] == product.name)

    dao.delete(inserted_product[0])

    new_product_list = dao.select_all()
    ids = [p[0] for p in new_product_list]

    assert inserted_product[0] not in ids