from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader, CSVLoader, PyPDFLoader



def webSiteLoader(url):
    loader = WebBaseLoader(url)
    return loader.load()

def csvFileLoader(file_path):
    docs = []
    for file in file_path:
        loader = CSVLoader(file_path=file)
        docs.extend(loader.load())
    return docs

def PDFFileLoader(pdfFile):
    docs = []
    for file in pdfFile:
        loader = PyPDFLoader(file_path=file)
        docs.extend(loader.load())
    return docs



llm = OllamaLLM(model="llama3.2:latest")

## load documents
docs = webSiteLoader("https://docs.smith.langchain.com/")

print(f"Total documents loaded: {len(docs)}")

## vectorize documents

embeddings = OllamaEmbeddings(model="nomic-embed-text")
text_splitter = RecursiveCharacterTextSplitter()
split_documents = text_splitter.split_documents(docs)
vector_store = Chroma.from_documents(
    documents=split_documents,
    embedding=embeddings,
    collection_name="smith_docs"
)
context = vector_store.as_retriever()

print (context)

chat_history = []

promptTemplate = ChatPromptTemplate.from_messages([
    ("system", """eres una Inteligencia artificial llamada Gabriela respondes preguntas con respuestas simples, ademas debes resolver preguntas acordes al contexto almacenado, trata al usuario por su nombre si no lo conoces preguntaselo al usuario"""),
     MessagesPlaceholder(variable_name="chat_history"),
    ("user", "<context>\n{context}\n</context>\n\nQuestion: {input}"),
])

chain = promptTemplate | llm






def chat():
    while True:
        user_input = input("Escribe tu pregunta (o 'salir' para terminar, 'historial' para ver el historial): ")
        if user_input.lower() == "salir":
            return
        if user_input.lower() == "historial":
            print("\n=== Historial de chat ===")
            for i, msg in enumerate(chat_history):
                tipo = "Usuario" if isinstance(msg, HumanMessage) else "Gabriela"
                print(f"{i+1}. {tipo}: {msg.content}")
            print("========================\n")
            continue

        retrieved_docs = context.get_relevant_documents(user_input) 
        contexto = "\n".join([doc.page_content for doc in retrieved_docs])       

        response = chain.invoke({"input": user_input, "chat_history": chat_history, "context": contexto})

        # Agregar el mensaje del usuario a la historia del chat
        chat_history.append(HumanMessage(content=user_input))
        # Agregar la respuesta de la IA a la historia del chat
        chat_history.append(AIMessage(content=response))

        # Imprimir la respuesta de la IA
        print("=" * 50)
        print("Gabriela:", response)
        print("=" * 50)


chat()