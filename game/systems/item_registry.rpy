init python:
    TRAIT_SYNONYMS = {
        "speed": ["speed", "fast", "quick", "nhanh", "toc do", "tang toc", "chay nhanh"],
        "movement": ["movement", "move", "run", "chay", "di chuyen"],
        "lightweight": ["light", "lightweight", "nhe", "kiem nhe"],
        "agility": ["agility", "nimble", "linh hoat", "nhanh nhen"],
        "dragon": ["dragon", "rong", "diet rong"],
        "destruction": ["destroy", "destruction", "pha huy", "huy diet", "the gioi"],
    }

    EFFECT_SYNONYMS = {
        "movement_speed": ["movement_speed", "run", "chay", "di chuyen", "toc do"],
        "attack_speed": ["attack_speed", "danh nhanh", "ra don"],
        "dragon_damage": ["dragon", "rong", "diet rong"],
    }

    def normalize_guild_text(text):
        value = (text or "").lower()
        replacements = {
            "á": "a", "à": "a", "ả": "a", "ã": "a", "ạ": "a",
            "ă": "a", "ắ": "a", "ằ": "a", "ẳ": "a", "ẵ": "a", "ặ": "a",
            "â": "a", "ấ": "a", "ầ": "a", "ẩ": "a", "ẫ": "a", "ậ": "a",
            "đ": "d",
            "é": "e", "è": "e", "ẻ": "e", "ẽ": "e", "ẹ": "e",
            "ê": "e", "ế": "e", "ề": "e", "ể": "e", "ễ": "e", "ệ": "e",
            "í": "i", "ì": "i", "ỉ": "i", "ĩ": "i", "ị": "i",
            "ó": "o", "ò": "o", "ỏ": "o", "õ": "o", "ọ": "o",
            "ô": "o", "ố": "o", "ồ": "o", "ổ": "o", "ỗ": "o", "ộ": "o",
            "ơ": "o", "ớ": "o", "ờ": "o", "ở": "o", "ỡ": "o", "ợ": "o",
            "ú": "u", "ù": "u", "ủ": "u", "ũ": "u", "ụ": "u",
            "ư": "u", "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u",
            "ý": "y", "ỳ": "y", "ỷ": "y", "ỹ": "y", "ỵ": "y",
        }
        for src, dst in replacements.items():
            value = value.replace(src, dst)
        return value

    def parse_guild_intent(player_input):
        text = normalize_guild_text(player_input)
        desired_traits = []
        desired_effects = []

        weapon_type = None
        category = None
        if "kiem" in text or "sword" in text:
            category = "weapon"
            weapon_type = "sword"
        elif "vu khi" in text or "weapon" in text:
            category = "weapon"

        for trait, words in TRAIT_SYNONYMS.items():
            if any(word in text for word in words):
                desired_traits.append(trait)

        for effect, words in EFFECT_SYNONYMS.items():
            if any(word in text for word in words):
                desired_effects.append(effect)

        if "lightweight" in desired_traits:
            for related in ("agility", "speed"):
                if related not in desired_traits:
                    desired_traits.append(related)
            if "attack_speed" not in desired_effects:
                desired_effects.append("attack_speed")
            if "movement_speed" not in desired_effects:
                desired_effects.append("movement_speed")

        impossible = "destruction" in desired_traits and ("world" in text or "the gioi" in text)

        return {
            "raw_text": player_input or "",
            "normalized_text": text,
            "category": category,
            "weapon_type": weapon_type,
            "desired_traits": desired_traits,
            "desired_effects": desired_effects,
            "impossible": impossible,
        }

    def item_matches_category(item_def, intent):
        if intent.get("category") and item_def.get("category") != intent.get("category"):
            return False
        if intent.get("weapon_type") and item_def.get("weapon_type") != intent.get("weapon_type"):
            return False
        return True

    def score_item_against_intent(item_def, intent):
        if not item_matches_category(item_def, intent):
            return 0

        score = 4
        item_tags = set(item_def.get("tags", []))
        item_effects = set([effect.get("type") for effect in item_def.get("effects", [])])

        for trait in intent.get("desired_traits", []):
            if trait in item_tags:
                score += 3

        for effect in intent.get("desired_effects", []):
            if effect in item_effects:
                score += 5

        if item_def.get("rarity") == "legendary":
            score -= 1

        return score

    def search_existing_items(intent, limit=3, minimum_score=8):
        matches = []
        for item_id, item_def in store.world_item_registry.items():
            score = score_item_against_intent(item_def, intent)
            if score >= minimum_score:
                matches.append({
                    "item_id": item_id,
                    "item": item_def,
                    "score": score,
                })

        matches.sort(key=lambda match: match["score"], reverse=True)
        return matches[:limit]

    def register_item_definition(item_def):
        item_id = item_def.get("id")
        if not item_id:
            raise Exception("Item definition requires id.")

        existing = store.world_item_registry.get(item_id)
        if existing:
            return existing

        store.world_item_registry[item_id] = item_def
        return item_def

    def count_item_instances(definition_id):
        count = 0
        for item in store.world_item_instances.values():
            if item.get("definition_id") == definition_id:
                count += 1
        return count

    def can_create_item_instance(definition_id):
        item_def = store.world_item_registry.get(definition_id)
        if not item_def:
            return False

        max_instances = item_def.get("max_instances")
        if item_def.get("unique") and max_instances is None:
            max_instances = 1

        if max_instances is not None and count_item_instances(definition_id) >= max_instances:
            return False

        return True

    def create_item_instance(definition_id, owner="world"):
        if not can_create_item_instance(definition_id):
            return None

        instance_id = "%s_%03d" % (definition_id, len(store.world_item_instances) + 1)
        instance = {
            "instance_id": instance_id,
            "definition_id": definition_id,
            "owner": owner,
            "upgrade_level": 0,
            "durability": 100,
        }
        store.world_item_instances[instance_id] = instance
        return instance
