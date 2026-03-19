# Live readiness

- **Project:** Autonomous Public Goods Chef
- **Track:** Protocol Labs Let the Agent Cook
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:10+00:00`

## Trust boundaries

- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **Slice** — `rest_json` — Drive checkout hooks and storefront policy changes.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.

## Offline-ready partner paths

- **ERC-8004 Receipts** — prepared_contract_call
- **Filecoin** — prepared_filecoin_bundle
- **ENS** — prepared_contract_call
- **Lido** — prepared_contract_call

## Live-only partner blockers

- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **Slice**: SLICE_API_KEY, SLICE_HOOK_URL — https://docs.slice.so/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/

## Highest-sensitivity actions

- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.
- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for AutonomousChefController.
- Run python3 scripts/run_agent.py to produce a dry run for autonomous_chef.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
