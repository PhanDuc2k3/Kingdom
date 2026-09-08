init python:
    def build_acquisition_quest(item_def):
        item_id = item_def.get("id")
        quest_id = "quest_acquire_%s" % item_id
        existing = store.guild_quests.get(quest_id)
        if existing:
            return existing

        acquisition = item_def.get("acquisition", {})
        material = acquisition.get("material", "vật liệu hiếm")
        source = acquisition.get("source", "wind_wolf_king")
        region = acquisition.get("region", "gale_forest")
        blacksmith = acquisition.get("blacksmith", "border_blacksmith")

        quest = {
            "id": quest_id,
            "title": "Dấu chân của Phong Lang",
            "description": "Thu thập nguyên liệu cần thiết để chế tạo %s." % item_def.get("name", item_id),
            "status": "proposed",
            "item_definition_id": item_id,
            "required_rank": acquisition.get("required_rank", "D"),
            "steps": [
                {"type": "travel", "target": region},
                {"type": "investigate", "target": "wind_wolf_den"},
                {"type": "defeat_boss", "target": source},
                {"type": "loot_material", "target": material},
                {"type": "craft", "target": blacksmith},
            ],
        }
        store.guild_quests[quest_id] = quest
        return quest

    def accept_guild_quest(quest_id):
        quest = store.guild_quests.get(quest_id)
        if not quest:
            return False
        quest["status"] = "active"
        if quest_id not in store.active_guild_quest_ids:
            store.active_guild_quest_ids.append(quest_id)
        guild_remember_quest(quest_id)
        return True

    def decline_guild_quest(quest_id):
        quest = store.guild_quests.get(quest_id)
        if not quest:
            return False
        quest["status"] = "declined"
        return True
