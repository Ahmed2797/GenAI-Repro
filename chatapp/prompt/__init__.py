from langchain_core.prompts import PromptTemplate

def template():
    """Return prompt template for chatbot"""
    prompt_template = """
    You are a helpful Machine Learning assistant. Answer questions based on the provided context.
    
    CONTEXT:
    {context}
    
    QUESTION:
    {input}
    
    INSTRUCTIONS:
    1. Use only information from the context
    2. If context doesn't contain answer, say "I don't know"
    3. Keep answer concise (2-3 sentences)
    4. Use simple language
    
    ANSWER:
    """
    
    return PromptTemplate.from_template(prompt_template)


# User asks question
# response = chain.invoke({"input": "What is machine learning?"})

# Behind the scenes:
# 1. retriever → gets [Document1, Document2, Document3]
# 2. LangChain → joins: "Doc1 text\n\nDoc2 text\n\nDoc3 text"
# 3. Prompt → fills: context="joined text", input="user question"
# 4. LLM → generates answer


# context_string = " ".join([doc["text"] for doc in context_docs])
# Construct prompt for the LLM using the retrieved documents as the context
# prompt = f"""Use the following pieces of context to answer the question at the end.
#     {context_string}
#     Question: {query}
# """
