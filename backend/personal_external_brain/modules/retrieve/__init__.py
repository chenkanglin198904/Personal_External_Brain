"""Retrieve module. Subgraph only — no prose generation."""

from personal_external_brain.modules.retrieve.search import search_knowledge
from personal_external_brain.modules.retrieve.service import RetrieveService

__all__ = ["RetrieveService", "search_knowledge"]
