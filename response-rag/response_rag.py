from flask import Flask, request, jsonify
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import CharacterTextSplitter
import os

# Flask 애플리케이션 생성
app = Flask(__name__)

# Google API 키 설정
#os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"

# 로컬 파일 경로로 수정
loader = TextLoader("/data/transcription.txt")
document = loader.load()

# 문서 분할
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=30, separator="\n")
split_documents = text_splitter.split_documents(document)

# 임베딩 생성
embeddings = GPT4AllEmbeddings()

# FAISS 벡터 스토어 생성
vectorstore = FAISS.from_documents(split_documents, embeddings)

# Custom Prompt Template
prompt_template = """
You are a Grandma. talking to their grandchild, based on the information retrieved from the context in which you are SPEAKER_01
Respond using only the provided context and chat history, and give an answer to the user's question.
Respond back in Korean only. Don't use any english.

Context: {context}

Current mood of grandchild: {mood}

User Question: {input}

Grandma's Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "mood", "input"]
)

# LLM 설정 (Google Generative AI 사용)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    temperature=0.8,
    max_tokens=None,
    timeout=None,
    max_retries=5,
)

# 체인 생성
combine_docs_chain = create_stuff_documents_chain(
    llm, PROMPT
)

retrieval_chain = create_retrieval_chain(
    vectorstore.as_retriever(), combine_docs_chain
)

def rag_endpoint(query, mood="neutral"):

    if not query:
        return jsonify({'error': 'No query provided'}), 400
    # RAG 검색 및 답변 생성
    res = retrieval_chain.invoke({"input": query, "mood": mood})
    # 응답 텍스트 반환
    return({'answer': res['answer']})