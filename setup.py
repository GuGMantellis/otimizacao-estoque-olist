# -*- coding: utf-8 -*-
"""
setup.py - Prepara o ambiente antes de rodar o notebook.
Execute: py setup.py
"""

import subprocess
import sys
import os
from pathlib import Path


def instalar(pacote):
    print(f"  instalando {pacote}...", end=" ", flush=True)
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", pacote, "-q"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("ok")
    else:
        print(f"FALHOU: {result.stderr.strip()[:60]}")


print("=" * 50)
print("  Setup - Analise de Estoque e Previsao de Demanda")
print("=" * 50)

# 1. Criar pastas necessarias
print("\n[1/3] Criando pastas...")
Path("data").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
print("  data/ e output/ prontas")

# 2. Instalar dependencias
print("\n[2/3] Instalando dependencias (pode demorar na primeira vez)...")
pacotes = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "prophet>=1.1.4",
    "jupyter>=1.0.0",
    "notebook>=7.0.0",
    "openpyxl>=3.1.0",
    "ipykernel>=6.0.0",
]
for p in pacotes:
    instalar(p)

# 3. Verificar dados
print("\n[3/3] Verificando pasta data/...")
esperados = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_products_dataset.csv",
    "olist_customers_dataset.csv",
]
categoria_ok = (
    Path("data/product_category_name_translation.csv").exists()
    or Path("data/olist_product_category_name_translation.csv").exists()
)
tudo_ok = True

for arq in esperados:
    existe = Path(f"data/{arq}").exists()
    status = "ok" if existe else "FALTANDO"
    print(f"  {arq}: {status}")
    if not existe:
        tudo_ok = False

print(f"  product_category_name_translation.csv: {'ok' if categoria_ok else 'FALTANDO'}")
if not categoria_ok:
    tudo_ok = False

print("\n" + "=" * 50)
if tudo_ok:
    print("  Tudo pronto! Para rodar o notebook:")
    print("  -> py -m jupyter notebook analise_estoque_olist.ipynb")
else:
    print("  Baixe os dados em:")
    print("  https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")
    print("  e coloque os .csv na pasta data/")
print("=" * 50)
