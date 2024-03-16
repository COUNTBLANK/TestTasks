import pyspark


products.join(prod_cat, products.id == prod_cat.product.id,'left')\
    .join(categories, product.categoty_id == category.id,'left').show(10)