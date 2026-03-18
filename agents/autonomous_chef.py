"""Project-specific context for Autonomous Public Goods Chef."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Autonomous Public Goods Chef",
    "track": "Protocol Labs Let the Agent Cook",
    "pitch": "A no-human-input swarm that discovers public-goods funding gaps, plans a bounded intervention, executes a dry-run-validated action, verifies impact, and self-files receipts.",
    "overlap_targets": [
        "ERC-8004 Receipts",
        "Venice Private Agents",
        "Filecoin",
        "Slice",
        "ENS",
        "Bankr Gateway",
        "Lido stETH Treasury"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
