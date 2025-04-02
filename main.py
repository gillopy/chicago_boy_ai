from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="deepseek-r1:1.5b", temperature=0.3, max_tokens=512)

template = """
Eres un asistente útil que responde preguntas sobre economia basándote en un conjunto de datos.
Debes utilizar el conjunto de datos para responder las preguntas, no debes
proporcionar ninguna información que no esté en las fuentes proporcionadas.

A continuación, se presentan algunos registros relevantes que pueden ayudarte a proporcionar una respuesta precisa y detallada:
{records}

Por favor, analiza la información y responde a la siguiente pregunta de manera clara y concisa:
Pregunta: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Escribe tu pregunta (q para salir): ")
    print("\n\n")
    if question == "q":
        break
    
    records = retriever.invoke(question)
    result = chain.invoke({"records": records, "question": question})
    print(result)