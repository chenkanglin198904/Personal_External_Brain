from personal_external_brain.llm.client import apply_caller


def test_apply_caller_adds_field() -> None:
    body = apply_caller({"model": "gpt-5-mini"}, "personal_external_brain")
    assert body["caller"] == "personal_external_brain"


def test_apply_caller_skips_blank() -> None:
    body = apply_caller({"model": "gpt-5-mini"}, "  ")
    assert "caller" not in body
