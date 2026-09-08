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
                "name": "Phong Hành Kiếm",
                "category": "weapon",
                "weapon_type": "sword",
                "rarity": "epic",
                "base_attack": 52,
                "tags": ["speed", "movement", "lightweight", "agility", "wind"],
                "effects": [
                    {"type": "movement_speed", "value": 6, "unit": "percent"},
                ],
                "passive": {
                    "name": "Khinh Bộ",
                    "type": "stamina_efficiency",
                    "description": "Khi mang kiếm, động tác né tránh ít tiêu hao thể lực hơn.",
                },
                "unique_skill": {
                    "name": "Phong Bộ",
                    "type": "movement_buff",
                    "description": "Sau khi né tránh thành công, tốc độ di chuyển tăng trong thời gian ngắn.",
                },
                "lore": "Một thanh kiếm nhẹ được rèn bằng Ngân Phong Thạch từ Phong Lang Vương.",
                "description": "Thanh kiếm nhanh dành cho người coi trọng bước chân hơn sức mạnh thô.",
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
                "name": "Long Sát Kiếm",
                "category": "weapon",
                "weapon_type": "sword",
                "rarity": "legendary",
                "base_attack": 58,
                "tags": ["dragon", "boss", "legendary"],
                "effects": [
                    {"type": "dragon_damage", "value": 15, "unit": "percent"},
                ],
                "passive": {
                    "name": "Long Khắc",
                    "type": "dragon_damage",
                    "description": "Gây thêm sát thương lên kẻ địch long tộc.",
                },
                "unique_skill": {
                    "name": "Phá Long Kích",
                    "type": "armor_break",
                    "description": "Kỹ thuật hiếm có dùng để phá lớp vảy rồng.",
                },
                "lore": "Những sổ ghi chép cổ nhất của Hội chỉ nhắc tới một thanh kiếm như vậy.",
                "description": "Một thanh kiếm huyền thoại chuyên khắc chế rồng. Sức mạnh thật sự phụ thuộc vào nâng cấp và khả năng làm chủ.",
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
            "name": "Kiếm Luyện Tập của Hội",
            "category": "weapon",
            "weapon_type": intent.get("weapon_type") or "sword",
            "rarity": "common",
            "base_attack": 18,
            "tags": ["training"],
            "effects": [],
            "description": "Vũ khí luyện tập cân bằng được Hội cất giữ.",
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
                "message": "Có ghi chép về %s, nhưng Hạng %s hiện tại của ngài chưa đủ để tiếp cận." % (item.get("name"), store.guild_rank),
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
            "message": "Có %s trong ghi chép của Hội. Nếu ngài muốn, Hội có thể lập nhiệm vụ lấy nguyên liệu để chế tạo." % item.get("name"),
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
            "message": "Lần trước chúng ta đã nói về %s. Vật liệu chính là %s." % (
                item.get("name"),
                guild_display_name(item.get("acquisition", {}).get("material", "vật liệu hiếm")),
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
                "message": "Không tồn tại loại vũ khí phá vỡ luật thế giới trong ghi chép của Hội.",
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
                "message": "Hội không tìm thấy phương án hợp lệ cho yêu cầu này.",
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
                "message": "Đề xuất bị từ chối vì vượt giới hạn cân bằng của thế giới.",
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
            message = "Có ghi chép về %s, nhưng điều kiện hiện tại chưa đủ để tiếp cận." % item.get("name")
        else:
            quest = build_acquisition_quest(item)
            guild_remember_quest(quest["id"])
            store.guild_pending_quest_id = quest["id"]
            message = "Hội có thể đề xuất %s. Cần %s, thường liên quan đến %s." % (
                item.get("name"),
                guild_display_name(item.get("acquisition", {}).get("material", "vật liệu hiếm")),
                guild_display_name(item.get("acquisition", {}).get("source", "nguồn chưa rõ")),
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
