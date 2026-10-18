#!/usr/bin/env python3
import json
import sys
from client import PersonalAgentGiftCuratorRecommender

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        curator = PersonalAgentGiftCuratorRecommender()
        profile = {"name": "Evelyn", "relationship_tier": "PARTNER", "interests": ["tea", "wellness"]}
        res = curator.curate_personalized_gift(profile, "Birthday", budget_limit_usd=100.0)
        assert "Matcha" in res["selected_gift"] or "Lamp" in res["selected_gift"]
        assert "Evelyn" in res["bespoke_greeting_card_copy"]
        print(f"[TEST PASS] Gift Curated: {res['selected_gift']} (${res['gift_price_usd']})")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-gift-curator", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "curate_personalized_gift", "description": "Curate personalized gifts and custom card copy"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                curator = PersonalAgentGiftCuratorRecommender()
                out = curator.curate_personalized_gift(args.get("recipient_profile", {}), args.get("occasion", "Celebration"), float(args.get("budget_limit_usd", 150.0)))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
