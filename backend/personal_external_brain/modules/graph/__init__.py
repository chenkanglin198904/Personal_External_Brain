"""Graph module. Storage only — no LLM."""

from personal_external_brain.modules.graph.factory import build_graph_store
from personal_external_brain.modules.graph.store import InMemoryGraphStore

__all__ = ["InMemoryGraphStore", "build_graph_store"]
