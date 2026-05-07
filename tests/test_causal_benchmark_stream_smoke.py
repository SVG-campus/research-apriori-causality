"""Smoke: HF CausalReasoningBenchmark streams and exposes expected columns."""

from __future__ import annotations

from datasets import load_dataset


def test_causal_reasoning_benchmark_stream_schema() -> None:
    rows = list(
        load_dataset(
            "syrgkanislab/CausalReasoningBenchmark",
            "causal_queries",
            split="train",
            streaming=True,
        ).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "effect" in r and "causal_question" in r
        assert isinstance(r["effect"], (int, float))
