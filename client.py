class PersonalizedUpsellRecommenderEngineClient:
    def get_upsells(self, last_item_category: str) -> dict:
        return {"recommendations": ["Premium Case", "Extra Charger"]}