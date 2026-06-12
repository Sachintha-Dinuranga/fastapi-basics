from fastapi import FastAPI

app = FastAPI()

# list of products
products = [
    
]

@app.get("/")
async def root():
    return {"message": "Hello World!!!"}

# get all the products
@app.get("/products")
def get_all_products():
    return "all products"
