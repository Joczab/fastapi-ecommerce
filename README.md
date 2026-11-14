# ecommerce-api

## Comandos

```bash
# Crear entorno virtual (venv)
python -m venv <nombre del entorno>

# Ingresar al entorno virtual
.\venv\Scripts\activate

# Instalar FastAPI
pip install "fastapi[standard]"

# Crear requirements (parecido a package.json)
pip freeze > requirements.txt

# Inicializar servidor FastAPI
uvicorn src.app:app --host=127.0.0.1 --port=8000 --reload=True
```