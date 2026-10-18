"""
Personal Agent Gift Curator & Social Graph Recommender (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
from typing import Dict, Any, List, Optional

class PersonalAgentGiftCuratorRecommender:
    GIFT_CATALOG = [
        {"item": "Japanese Ceramic Matcha Whisk & Bowl Set", "category": "tea", "tier": ["PARTNER", "CLOSE_FRIEND"], "price": 68.0},
        {"item": "Noise-Cancelling Premium Travel Headphones", "category": "tech", "tier": ["PARTNER", "MENTOR"], "price": 249.0},
        {"item": "Handcrafted Leather Journal & Brass Fountain Pen", "category": "writing", "tier": ["MENTOR", "COLLEAGUE"], "price": 85.0},
        {"item": "Artisan Single-Origin Specialty Coffee Subscription", "category": "coffee", "tier": ["CLOSE_FRIEND", "COLLEAGUE"], "price": 45.0},
        {"item": "Smart Ambient Sunrise Sleep Wake-up Lamp", "category": "wellness", "tier": ["PARTNER", "CLOSE_FRIEND"], "price": 120.0}
    ]

    def __init__(self, curator_name: str = "GenPark-GiftCurator-Core"):
        self.curator_name = curator_name

    def curate_personalized_gift(self, recipient_profile: Dict[str, Any], occasion: str, budget_limit_usd: float = 150.0) -> Dict[str, Any]:
        name = recipient_profile.get("name", "Friend")
        tier = recipient_profile.get("relationship_tier", "CLOSE_FRIEND").upper()
        interests = [i.lower() for i in recipient_profile.get("interests", ["coffee", "wellness"])]
        
        candidates = []
        for g in self.GIFT_CATALOG:
            if g["price"] <= budget_limit_usd:
                match_score = (1.5 if tier in g["tier"] else 0.5) + (2.0 if any(it in g["category"] for it in interests) else 0.0)
                candidates.append((match_score, g))
                
        candidates.sort(key=lambda x: x[0], reverse=True)
        top_gift = candidates[0][1] if candidates else {"item": "Thoughtful Handwritten Card & Specialty Gift Voucher", "price": 50.0}
        
        # Bespoke greeting message synthesis
        card_copy = (
            f"Dear {name},\n"
            f"Warmest wishes on your {occasion}! Knowing your love for {interests[0] if interests else 'life'}, "
            f"I picked this {top_gift['item']} hoping it brings you joy and inspiration.\n"
            f"Cheers to your next chapter!"
        )
        
        return {
            "curator": self.curator_name,
            "recipient_name": name,
            "occasion": occasion,
            "selected_gift": top_gift["item"],
            "gift_price_usd": top_gift["price"],
            "bespoke_greeting_card_copy": card_copy,
            "total_candidates_evaluated": len(candidates),
            "verdict": "PERSONALIZED_GIFT_CURATED"
        }
