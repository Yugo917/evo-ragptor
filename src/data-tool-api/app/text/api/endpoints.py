from fastapi import APIRouter, Depends, Query
from dependency_injector.wiring import inject, Provide
from app.container import Container
from app.text.api.request_models import CompareRequest
from app.text.business.text_comparer import TextComparer

router = APIRouter(prefix="/text", tags=["Text"])


@router.post("/compare/all-methods", summary="Compare two strings using all available methods")
@inject
def compare_all_methods(
    payload: CompareRequest,
    text_comparer: TextComparer = Depends(Provide[Container.text_comparer]),
):
    return text_comparer.compare_all_methods(payload.text1, payload.text2)


@router.post("/compare/fuzzy", summary="Compare two strings using fuzzy string matching")
@inject
def compare_fuzzy(
    payload: CompareRequest,
    text_comparer: TextComparer = Depends(Provide[Container.text_comparer]),
):
    return {"fuzzy_score": text_comparer.compare_fuzzy(payload.text1, payload.text2)}


@router.post("/compare/embedding", summary="Compare two strings using embedding cosine similarity")
@inject
def compare_embedding(
    payload: CompareRequest,
    text_comparer: TextComparer = Depends(Provide[Container.text_comparer]),
):
    return {
        "embedding_cosine_score": text_comparer.compare_embeddings(payload.text1, payload.text2)
    }


@router.post("/compare/crossencoder", summary="Compare two strings using cross-encoder")
@inject
def compare_crossencoder(
    payload: CompareRequest,
    text_comparer: TextComparer = Depends(Provide[Container.text_comparer]),
):
    return {
        "crossencoder_score": text_comparer.compare_crossencoder(payload.text1, payload.text2)
    }

