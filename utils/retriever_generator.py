from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def retriever_generator(vectorstore,query, llm):

    retriever = vectorstore.as_retriever()

    prompt = PromptTemplate.from_template(
        "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If the answer is not in the context, just say that you don't know. Use three sentences maximum and keep the answer concise.\nQuestion: {question} \nContext: {context} \nAnswer:"
    )
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    answer = rag_chain.invoke(query)
    return answer
