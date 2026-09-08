init python:
    def build_guild_context(intent):
        return {
            "player_level": store.player_level,
            "guild_rank": store.guild_rank,
            "unlocked_regions": list(store.guild_unlocked_regions),
            "known_dungeons": list(store.guild_known_dungeons),
            "known_bosses": list(store.guild_known_bosses),
            "known_blacksmiths": list(store.guild_known_blacksmiths),
            "recent_messages": list(store.guild_recent_messages),
            "discussed_item_ids": list(store.guild_discussed_item_ids),
            "intent": intent,
        }

    def mock_generate_item_proposal(intent, context):
        traits = intent.get("desired_traits", [])
        effects = intent.get("desired_effects", [])

        if intent.get("impossible"):
            return None

        if intent.get("weapon_type") == "sword" and ("movement_speed" in effects or "speed" in traits or "lightweight" in traits):
            return {
                "id": "windwalker_sword",
                "name": "Phong Hanh Kiem",
                "category": "weapon",
                "weapon_type": "sword",
                "rarity": "epic",
                "base_attack": 52,
                "tags": ["speed", "movement", "lightweight", "agility", "wind"],
                "effects": [
                    {"type": "movement_speed", "value": 6, "unit": "percent"},
                ],
                "passive": {
                    "name": "Light Step",
                    "type": "stamina_efficiency",
                    "description": "Dodging feels less costly while carrying the blade.",
                },
                "unique_skill": {
                    "name": "Phong Bo",
                    "type": "movement_buff",
                    "description": "After a successful dodge, movement speed rises briefly.",
                },
                "lore": "A light blade forged with silver wind stone from the Wind Wolf King.",
                "description": "A swift sword for adventurers who value footwork over brute force.",
                "acquisition": {
                    "type": "craft",
                    "material": "silver_wind_stone",
                    "source": "wind_wolf_king",
                    "region": "gale_forest",
                    "blacksmith": "border_blacksmith",
                    "required_rank": "D",
                },
                "upgrade": {
                    "attack_per_level": 3,
                    "max_level": 5,
                    "skill_upgrade_supported": True,
                },
                "unique": False,
                "max_instances": None,
            }

        if "dragon" in traits:
            return {
                "id": "dragon_slayer",
                "name": "Dragon Slayer",
                "category": "weapon",
                "weapon_type": "sword",
                "rarity": "legendary",
                "base_attack": 58,
                "tags": ["dragon", "boss", "legendary"],
                "effects": [
                    {"type": "dragon_damage", "value": 15, "unit": "percent"},
                ],
                "passive": {
                    "name": "Dragon Bane",
                    "type": "dragon_damage",
                    "description": "Deals more damage to dragon-type enemies.",
                },
                "unique_skill": {
                    "name": "Dragon Breaker",
                    "type": "armor_break",
                    "description": "A rare technique for cracking dragon scales.",
                },
                "lore": "Only one such sword is recorded in the oldest guild ledgers.",
                "description": "A legendary anti-dragon blade. Its true power depends on upgrades and mastery.",
                "acquisition": {
                    "type": "drop",
                    "source": "ancient_dragon",
                    "required_rank": "A",
                },
                "upgrade": {
                    "attack_per_level": 3,
                    "max_level": 10,
                    "skill_upgrade_supported": True,
                },
                "unique": True,
                "max_instances": 1,
            }

        return {
            "id": "guild_practice_blade",
            "name": "Guild Practice Blade",
            "category": "weapon",
            "weapon_type": intent.get("weapon_type") or "sword",
            "rarity": "common",
            "base_attack": 18,
            "tags": ["training"],
            "effects": [],
            "description": "A balanced training weapon kept by the guild.",
            "acquisition": {
                "type": "guild_shop",
                "required_rank": "D",
            },
            "upgrade": {
                "attack_per_level": 2,
                "max_level": 3,
                "skill_upgrade_supported": False,
            },
            "unique": False,
            "max_instances": None,
        }

    def guild_response_for_existing_item(match, matches=None):
        item = match["item"]
        matches = matches or [match]
        store.guild_pending_item_id = item["id"]
        guild_remember_item(item["id"])

        progression = validate_progression_rules(item)
        if progression.get("availability") == "locked":
            store.guild_pending_quest_id = None
            return {
                "status": "locked",
                "kind": "existing_item",
                "item": item,
                "matches": matches,
                "quest": None,
                "message": "Co ghi chep ve %s, nhung Rank %s hien tai chua du de tiep can." % (item.get("name"), store.guild_rank),
            }

        quest = build_acquisition_quest(item)
        store.guild_pending_quest_id = quest["id"]
        guild_remember_quest(quest["id"])
        return {
            "status": "available",
            "kind": "existing_item",
            "item": item,
            "matches": matches,
            "quest": quest,
            "message": "Co %s trong ghi chep cua Hoi. Neu ngai muon, Hoi co the lap nhiem vu lay nguyen lieu de che tao." % item.get("name"),
        }

    def guild_recall_previous_discussion(intent):
        text = intent.get("normalized_text", "")
        if "lan truoc" not in text and "truoc" not in text:
            return None
        if not store.guild_discussed_item_ids:
            return None
        item_id = store.guild_discussed_item_ids[-1]
        item = store.world_item_registry.get(item_id)
        if not item:
            return None
        return {
            "status": "available",
            "kind": "memory",
            "item": item,
            "quest": store.guild_quests.get("quest_acquire_%s" % item_id),
            "message": "Lan truoc chung ta noi ve %s. Vat lieu chinh la %s." % (
                item.get("name"),
                item.get("acquisition", {}).get("material", "vat lieu hiem"),
            ),
        }

    def process_guild_player_input(player_input):
        guild_remember_message("player", player_input)
        intent = parse_guild_intent(player_input)
        store.guild_last_intent = intent

        if intent.get("impossible"):
            result = {
                "status": "impossible",
                "kind": "world_rule",
                "message": "Khong ton tai loai vu khi pha vo luat the gioi trong ghi chep cua Hoi.",
            }
            store.guild_last_result = result
            guild_remember_message("receptionist", result["message"])
            return result

        recalled = guild_recall_previous_discussion(intent)
        if recalled:
            store.guild_last_result = recalled
            guild_remember_message("receptionist", recalled["message"])
            return recalled

        matches = search_existing_items(intent)
        store.guild_last_search_results = matches
        if matches:
            result = guild_response_for_existing_item(matches[0], matches)
            store.guild_last_result = result
            guild_remember_message("receptionist", result["message"])
            return result

        context = build_guild_context(intent)
        proposal = mock_generate_item_proposal(intent, context)
        if not proposal:
            result = {
                "status": "impossible",
                "kind": "no_proposal",
                "message": "Hoi khong tim thay phuong an hop le cho yeu cau nay.",
            }
            store.guild_last_result = result
            guild_remember_message("receptionist", result["message"])
            return result

        validation = validate_item_proposal(proposal)
        if not validation.get("accepted"):
            result = {
                "status": "rejected",
                "kind": "balance_rejected",
                "proposal": proposal,
                "validation": validation,
                "message": "De xuat bi tu choi vi vuot gioi han can bang cua the gioi.",
            }
            store.guild_last_result = result
            guild_remember_message("receptionist", result["message"])
            return result

        item = register_item_definition(proposal)
        guild_remember_item(item["id"])
        store.guild_pending_item_id = item["id"]

        status = validation.get("availability", "available")
        if status == "locked":
            quest = None
            store.guild_pending_quest_id = None
            message = "Co ghi chep ve %s, nhung dieu kien hien tai chua du de tiep can." % item.get("name")
        else:
            quest = build_acquisition_quest(item)
            guild_remember_quest(quest["id"])
            store.guild_pending_quest_id = quest["id"]
            message = "Hoi co the de xuat %s. Can %s, thuong lien quan den %s." % (
                item.get("name"),
                item.get("acquisition", {}).get("material", "vat lieu hiem"),
                item.get("acquisition", {}).get("source", "nguon chua ro"),
            )

        result = {
            "status": status,
            "kind": "new_item",
            "item": item,
            "quest": quest,
            "validation": validation,
            "message": message,
        }
        store.guild_last_result = result
        guild_remember_message("receptionist", message)
        return result
