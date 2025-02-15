from llama_index.core.prompts import PromptTemplate

instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of the code should be a Python expression that can be called with `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression.
"""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is 'df'.
    This is the result of `print(df.head())`:
    {df_str}
    
    Follow these instructions:
    {instruction_str}
    Query: {query_str}
    
    **ONLY OUTPUT THE PYTHON EXPRESSION BELOW. DO NOT INCLUDE ANY OTHER TEXT.**
    
    Expression:"""
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about the world population statistics and details about a country."""