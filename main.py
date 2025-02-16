# ================== Embedding Model ==================
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings

local_embed_model = HuggingFaceEmbedding(
    model_name="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    device="cpu"
    )

Settings.embed_model = local_embed_model

# =====================================================


import os
from dotenv import load_dotenv
import pandas as pd
from llama_index.experimental.query_engine.pandas import PandasQueryEngine
# from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini
from prompts import instruction_str, new_prompt, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms import gemini
from pdf import pakistan_engine

load_dotenv()

population_path = os.path.join('data', 'world_population_23.csv')
population_df = pd.read_csv(population_path)

# To run on locally available LLMs
# ollama_llm = Ollama(model="deepseek-r1:1.5b", temperature=0.7, request_timeout=120)

# Using Gemini API
llm = Gemini(api_key=os.getenv("GEMINI_API_KEY"), model="models/gemini-1.5-flash")

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, llm=llm, instruction_str=instruction_str)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})
# population_query_engine.query("what is the population of Pakistan?")

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine, 
        metadata=ToolMetadata(
            name="population_data",
            description="This is the information about the world population and demographics."
        ),
    ),
    QueryEngineTool(
        query_engine=pakistan_engine, 
        metadata=ToolMetadata(
            name="pakistan_data",
            description="This is detailed information about the country called Pakistan."
        ),
    ),
]

llm = Gemini(model="models/gemini-1.5-flash")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while(prompt:=input("Enter a prompt (q to quite): ")) != 'q':
    result = agent.query(prompt)
    print(prompt)
