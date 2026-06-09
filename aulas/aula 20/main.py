import uvicorn
from fastapi import FastAPI

from controlador_cliente import router as clientes_router
from controlador_marca import router as marcas_router
from controlador_pedido import router as pedidos_router
from controlador_produto import router as produtos_router

app = FastAPI()

app.include_router(clientes_router)
app.include_router(marcas_router)
app.include_router(pedidos_router)
app.include_router(produtos_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = 80,
        reload=True
    )