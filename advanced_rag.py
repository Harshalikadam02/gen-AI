import concurrent.futures
from typing import Any, Dict, List, Tuple

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path


# ---------------------------------------------------------------------------
# utilities for retrieval
# ---------------------------------------------------------------------------

def parallel_retrieval(
    retriever: QdrantVectorStore,
    queries: List[str],
    top_k: int = 5,
) -> Dict[str, List[Any]]:
    """Run multiple similarity searches in parallel (fan‑out) and return a map
    from each query to the list of returned documents.

    This is useful when you want to explore different formulations of a question
    or query the same store concurrently from multiple agents.

    Parameters
    ----------
    retriever : QdrantVectorStore
        The vector store instance that implements ``similarity_search``.
    queries : List[str]
        A list of text queries to execute.
    top_k : int
        Number of nearest neighbours to return for each query.
    """
    results: Dict[str, List[Any]] = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_map = {
            executor.submit(retriever.similarity_search, q, k=top_k): q
            for q in queries
        }
        for future in concurrent.futures.as_completed(future_map):
            q = future_map[future]
            try:
                results[q] = future.result()
            except Exception:
                # if one query fails, record an empty list so caller can still
                # fuse the others
                results[q] = []
    return results


def reciprocal_rank_fusion(
    rankings: List[List[Any]],
    k: int = 60,
) -> List[Tuple[Any, float]]:
    """Combine multiple ranked lists using Reciprocal Rank Fusion (RRF).

    Each input ranking should be an ordered iterable of document identifiers
    (or any hashable token that uniquely identifies the returned item). The
    function assigns a score to each document by summing ``1/(k+rank+1)`` over
    all rankings in which the document appears.  Larger scores indicate higher
    consensus relevance.

    Parameters
    ----------
    rankings : List[List[Any]]
        A list of ranked lists.  For example, ``[[doc1, doc2], [doc2, doc3]]``.
    k : int
        The RRF parameter that controls how quickly the contribution of each
        position decays.  The default ``60`` matches the value used in many
        research papers.

    Returns
    -------
    List[Tuple[Any,float]]
        A list of ``(doc_id, score)`` tuples sorted in descending order by score.
    """
    scores: Dict[Any, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    # sort by score descending
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


# ---------------------------------------------------------------------------
# example setup (mirrors contents of rag_1.py but kept local for demonstration)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    pdf_path = Path(__file__).parent / "AIclasses.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key="OPENAI_API_KEY")
    store = QdrantVectorStore.from_documents(
        documents=[],
        url="http://localhost:6333",
        embeddings=embeddings,
        collection_name="learning_langchain",
    )
    store.add_documents(documents=split_docs)
    print("injection done in advanced_rag")

    retriever = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        embeddings=embeddings,
        collection_name="learning_langchain",
    )

    # run two queries in parallel and fuse results
    queries = ["What is Robotics?", "Define robotics"]
    parallel_results = parallel_retrieval(retriever, queries, top_k=3)
    print("parallel retrieval results:\n", parallel_results)

    # demonstrate reciprocal rank fusion on the document ids
    ranked_lists = [[chunk.metadata.get("page", i) for i, chunk in enumerate(parallel_results[q])] for q in queries]
    fused = reciprocal_rank_fusion(ranked_lists)
    print("fused rankings:\n", fused)
