"""Routing label rule for the AEQ project.

The routing target for each prompt is the cheapest model that still answered
well. "Answered well" means its score on that prompt cleared a quality
threshold. Nine of the ten Performance-Cost datasets score answers 0 or 1, so
the threshold mostly matters for arenahard, which also hands out 0.5 for a
draw. If no model cleared the threshold on a prompt, no amount of routing buys
a good answer, so the label falls back to the cheapest model overall: spend the
least on a lost cause.
"""

import pandas as pd


def assign_router_labels(long_df, threshold):
    """Return one row per prompt with the routing label.

    long_df needs columns: prompt_id, model, cost, score (one row per
    prompt-model pair, reference models already excluded).
    threshold is the minimum score that counts as a good answer.

    Output columns: prompt_id, label, label_cost, n_capable.
    """
    if not 0 < threshold <= 1:
        raise ValueError(f"threshold must be in (0, 1], got {threshold}")

    rows = []
    for prompt_id, group in long_df.groupby("prompt_id"):
        capable = group[group["score"] >= threshold]
        if len(capable) > 0:
            pick = capable.loc[capable["cost"].idxmin()]
        else:
            # nobody cleared the bar, so lose as little money as possible
            pick = group.loc[group["cost"].idxmin()]
        rows.append(
            {
                "prompt_id": prompt_id,
                "label": pick["model"],
                "label_cost": pick["cost"],
                "n_capable": len(capable),
            }
        )
    return pd.DataFrame(rows)
