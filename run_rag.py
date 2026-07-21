import traceback
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

try:
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import FAISS
except Exception:
    # Defer to runtime error reporting below
    pass


def main():
    try:
        with open('cppData.txt', 'r', encoding='utf-8') as f:
            txtData = f.read()
        print('Read cppData.txt (length:', len(txtData), ')')

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(txtData)
        finalDocuments = [Document(page_content=c) for c in chunks]
        print('Created', len(finalDocuments), 'document chunks')

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        print('Embeddings created')

        db = FAISS.from_documents(finalDocuments, embeddings)
        print('FAISS index created')

        query = "What is C++?"
        docs = db.similarity_search(query, k=3)
        print('Top matches:')
        for i, d in enumerate(docs):
            print('----', i)
            print(d.page_content[:500])

    except Exception as e:
        print('ERROR:')
        traceback.print_exc()


if __name__ == '__main__':
    main()
