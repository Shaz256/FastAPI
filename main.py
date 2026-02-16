from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine, get_db

# ✅ create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS (VERY IMPORTANT for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =============================
# GET PRODUCTS
# =============================
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


# =============================
# ADD PRODUCT
# =============================
@app.post("/products")
def add_product(product: dict, db: Session = Depends(get_db)):
    db_product = models.Product(
        name=product.get("name"),
        description=product.get("description"),
        price=product.get("price"),
        quantity=product.get("quantity"),
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# =============================
# DELETE PRODUCT
# =============================
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if product:
        db.delete(product)
        db.commit()

    return {"message": "Deleted"}
