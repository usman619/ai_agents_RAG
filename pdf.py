import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader 
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv

load_dotenv()

gemini_llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-1.5-flash")

def get_index(data, index_name):
    if not os.path.exists(index_name):
        print(f"Building index {index_name}")

        # gemini_llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-1.5-flash")
        index = VectorStoreIndex.from_documents(
            data,
            show_progress=True,
            llm=gemini_llm,
        )
        index.storage_context.persist(persist_dir=index_name)
    else:
        storage_ctx = StorageContext.from_defaults(persist_dir=index_name)
        index = load_index_from_storage(storage_ctx)
    return index


pdf_path = os.path.join('data','Pakistan.pdf')
pakistan_pdf = PDFReader().load_data(file=pdf_path)
# Then you can do:
pakistan_index = get_index(pakistan_pdf, "pakistan")

# Also pass the same LLM or a new one to as_query_engine
pakistan_engine = pakistan_index.as_query_engine(llm=gemini_llm)


# OpenAI Version
# def get_index(data, index_name):
#     index = None
    
#     if not os.path.exists(index_name):
#         print(f"Building index {index_name}")
#         index = VectorStoreIndex.from_documents(data, show_progress=True) # llm=None
#         index.storage_context.persist(persist_dir=index_name)


#     else:
#         storage_ctx = StorageContext.from_defaults(persist_dir=index_name)
#         index = load_index_from_storage(storage_ctx)

#     return index

# pdf_path = os.path.join('data','Pakistan.pdf')
# pakistan_pdf = PDFReader().load_data(file=pdf_path)

# pakistan_index = get_index(pakistan_pdf, "pakistan")
# pakistan_engine = pakistan_index.as_query_engine() # llm=None
