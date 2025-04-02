from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("deuda.csv")
df.columns = df.columns.str.strip()  # Elimina espacios en blanco en los nombres de columnas

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db_deuda"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        # Construir el contenido de cada documento con información clave de la deuda
        content = (
            f"Fecha: {row['fecha']}. "
            f"Saldos: {row['saldos']}. "
            f"Desembolsos: {row['desembolsos']}. "
            f"Pagos (cap e int): {row['pagos_cap_e_int']}. "
            f"Transferencia neta: {row['transferencia_neta']}."
        )
        document = Document(
            page_content=content,
            metadata={"fecha": row["fecha"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
vector_store = Chroma(
    collection_name="deuda_records",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)