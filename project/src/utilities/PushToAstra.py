from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

class PushToAstra:
    def __init__(self, api_key, model, token, api_endpoint, collection_name="vector_movies"):
        self.embeddings = OpenAIEmbeddings(api_key=api_key, model=model)
        self.vstore = AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name=collection_name,
            token=token,
            api_endpoint=api_endpoint
        )
        self.vstore.clear()

    def push(self, df):
        documents = []
        for index, row in df.iterrows():
            metadata = {"genres": row['genres']}
            document = Document(page_content=row['summary'], metadata=metadata)
            documents.append(document)
            if len(documents) == 15:
                inserted_ids = self.vstore.add_documents(documents)
                print(f"\nInserted {len(inserted_ids)} documents.")
                documents = []
                inserted_ids = []
                print(f"im at index: {index}")