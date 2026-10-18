from client import PersonalAgentGiftCuratorRecommender

def main():
    curator = PersonalAgentGiftCuratorRecommender()
    rec = {"name": "Marcus", "relationship_tier": "MENTOR", "interests": ["writing", "coffee"]}
    res = curator.curate_personalized_gift(rec, "Promotion", budget_limit_usd=120.0)
    print("--- Personal Gift Curator ---")
    print(f"Recipient: {res['recipient_name']} | Occasion: {res['occasion']}")
    print(f"Gift: {res['selected_gift']} (${res['gift_price_usd']})")
    print(f"Card Message:\n{res['bespoke_greeting_card_copy']}")

if __name__ == "__main__":
    main()
