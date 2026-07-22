"""Smoke tests for the routing label rule."""

import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from routing_label import assign_router_labels


def make_long_df():
    # two prompts, three models with distinct prices
    return pd.DataFrame(
        {
            "prompt_id": ["p1"] * 3 + ["p2"] * 3,
            "model": ["cheap", "mid", "pricey"] * 2,
            "cost": [0.001, 0.01, 0.1, 0.002, 0.02, 0.2],
            # p1: cheap fails, mid and pricey solve it -> label should be mid
            # p2: everyone fails -> fallback to cheapest
            "score": [0.0, 1.0, 1.0, 0.0, 0.0, 0.0],
        }
    )


def test_picks_cheapest_capable_model():
    labels = assign_router_labels(make_long_df(), threshold=1.0)
    p1 = labels[labels.prompt_id == "p1"].iloc[0]
    assert p1.label == "mid"
    assert p1.n_capable == 2


def test_falls_back_to_cheapest_when_nobody_clears():
    labels = assign_router_labels(make_long_df(), threshold=1.0)
    p2 = labels[labels.prompt_id == "p2"].iloc[0]
    assert p2.label == "cheap"
    assert p2.n_capable == 0


def test_label_is_a_known_model():
    df = make_long_df()
    labels = assign_router_labels(df, threshold=1.0)
    assert set(labels.label) <= set(df.model)


def test_rejects_bad_threshold():
    with pytest.raises(ValueError):
        assign_router_labels(make_long_df(), threshold=0)
