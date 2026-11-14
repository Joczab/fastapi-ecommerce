from pathlib import Path

# print(__file__)
# print(Path(__file__).parent.resolve())

SRC_DIR = Path(__file__).parent.parent
print(SRC_DIR)

STATIC_DIR = SRC_DIR / 'static'
print(STATIC_DIR)

# Absoluta
# C:\Users\clases.LABCOMP.001\Desktop\ecommerce-api\src\static

# Relative
# \src\static
