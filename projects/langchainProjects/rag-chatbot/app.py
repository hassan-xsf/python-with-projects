from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# https://blog.futuresmart.ai/langchain-rag-from-basics-to-production-ready-rag-chatbot

collection_name = "smiu-data"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def load_data():
    try:
        current_dir = Path(__file__).parent
        data_path = current_dir / "data" / "smiu-data.md"
        with open(data_path, "r", encoding="utf-8") as file:
            text_content = file.read()
            
        return text_content
    
    except FileNotFoundError:
        print("Error: Data file not found")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    text = load_data()
    if text:
        print("Data loaded successfully")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        splits = splitter.split_text(text)
        print(f"Split the file into {len(splits)} chunks.")
        document_embeddings = embeddings.embed_documents([split for split in splits])
        print(f"Created embeddings for {len(document_embeddings)} document chunks.")
        print(document_embeddings[0][:10])
        chrome_vector = Chroma.from_documents(
            collection_name=collection_name,
            documents=document_embeddings,
            embeddings=embeddings,
            persist_directory="./smiu-db"
        )
        print("Vector Store for collection {collection_name} has been created at ./smiu-db")

        query = "When was SMIU founded?"
        search_results = chrome_vector.similarity_search(query, k=2)
        
        print(f"\nTop 2 most relevant chunks for the query: '{query}'\n")
        for i, result in enumerate(search_results, 1):
            print(f"Result {i}:")
            print(f"Source: {result.metadata.get('source', 'Unknown')}")
            print(f"Content: {result.page_content}")