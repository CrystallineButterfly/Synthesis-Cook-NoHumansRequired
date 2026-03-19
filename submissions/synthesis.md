# Autonomous Public Goods Chef

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Cook-NoHumansRequired
- **Primary track:** Protocol Labs Let the Agent Cook
- **Overlap targets:** ERC-8004 Receipts, Venice Private Agents, Filecoin, Slice, ENS, Bankr Gateway, Lido stETH Treasury
- **Primary contract:** AutonomousChefController
- **Primary operator module:** autonomous_chef
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A no-human-input swarm that discovers public-goods funding gaps, plans a bounded intervention, executes a dry-run-validated action, verifies impact, and self-files receipts.

## Track evidence

- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`
- `artifacts/filecoin/0xc4912c5dd8c7d404a09afa18c6fe16cd84871c08e5c3537d8bb1b150e1dc4ed1.json`
- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/onchain_intents/lido_yield_route.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Autonomous Public Goods Chef",
  "track": "Protocol Labs Let the Agent Cook",
  "plan_id": "0xc4912c5dd8c7d404a09afa18c6fe16cd84871c08e5c3537d8bb1b150e1dc4ed1",
  "simulation_hash": "0xa7ed24b1d31d2ef8f150f72844536e23708d5d0854766103a1916500fb37bf40",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json",
    "artifacts/filecoin/0xc4912c5dd8c7d404a09afa18c6fe16cd84871c08e5c3537d8bb1b150e1dc4ed1.json",
    "artifacts/onchain_intents/ens_ens_publish.json",
    "artifacts/onchain_intents/lido_yield_route.json"
  ],
  "partner_statuses": {
    "ERC-8004 Receipts": "prepared_contract_call",
    "Venice": "awaiting_credentials",
    "Filecoin": "prepared_filecoin_bundle",
    "Slice": "awaiting_credentials",
    "ENS": "prepared_contract_call",
    "Bankr Gateway": "awaiting_credentials",
    "Lido": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:10+00:00"
}
```
