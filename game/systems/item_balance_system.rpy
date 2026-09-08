init python:
    RARITY_POWER_BUDGET = {
        "common": 10,
        "uncommon": 18,
        "rare": 28,
        "epic": 48,
        "legendary": 55,
        "mythic": 75,
    }

    EFFECT_POWER_COST = {
        "attack": 0.4,
        "movement_speed": 2.0,
        "attack_speed": 2.4,
        "crit": 2.2,
        "lifesteal": 4.0,
        "stun": 8.0,
        "slow": 2.5,
        "dash": 7.0,
        "aoe": 6.0,
        "dragon_damage": 1.3,
    }

    ITEM_PROPOSAL_FORBIDDEN_FIELDS = {
        "player_hp",
        "player_gold",
        "player_exp",
        "inventory",
        "story_stage",
        "relationship",
        "drop_rate",
        "legendary_granted",
        "quest_complete",
    }

    WORLD_POWER_RULES_BY_RANK = {
        "D": {
            "max_weapon_attack": 60,
            "max_movement_bonus": 8,
            "max_attack_speed": 8,
            "max_crit": 8,
            "max_stun_duration": 1.0,
            "max_skill_tier": 2,
        },
        "C": {
            "max_weapon_attack": 72,
            "max_movement_bonus": 12,
            "max_attack_speed": 12,
            "max_crit": 12,
            "max_stun_duration": 1.5,
            "max_skill_tier": 3,
        },
        "A": {
            "max_weapon_attack": 95,
            "max_movement_bonus": 20,
            "max_attack_speed": 18,
            "max_crit": 18,
            "max_stun_duration": 2.5,
            "max_skill_tier": 5,
        },
    }

    def _item_effect_value(effect):
        value = effect.get("value", 0)
        try:
            return float(value)
        except Exception:
            return 0.0

    def calculate_item_power(item_def):
        power = float(item_def.get("base_attack", 0)) * EFFECT_POWER_COST["attack"]

        for effect in item_def.get("effects", []):
            effect_type = effect.get("type")
            cost = EFFECT_POWER_COST.get(effect_type, 1.0)
            power += _item_effect_value(effect) * cost

        if item_def.get("unique_skill"):
            power += 8.0
        if item_def.get("passive"):
            power += 4.0

        return power

    def validate_item_balance(item_def):
        rarity = item_def.get("rarity", "common")
        budget = RARITY_POWER_BUDGET.get(rarity)
        if budget is None:
            return {
                "accepted": False,
                "reason": "unknown_rarity",
                "power": 0,
                "budget": 0,
            }

        power = calculate_item_power(item_def)
        if power > budget:
            return {
                "accepted": False,
                "reason": "power_budget_exceeded",
                "power": power,
                "budget": budget,
            }

        return {
            "accepted": True,
            "reason": "ok",
            "power": power,
            "budget": budget,
        }

    def validate_world_rules(item_def):
        rules = WORLD_POWER_RULES_BY_RANK.get(store.guild_rank, WORLD_POWER_RULES_BY_RANK["D"])
        if item_def.get("category") == "weapon" and item_def.get("base_attack", 0) > rules["max_weapon_attack"]:
            return {
                "accepted": False,
                "reason": "weapon_attack_too_high",
            }

        for effect in item_def.get("effects", []):
            effect_type = effect.get("type")
            value = _item_effect_value(effect)
            if effect_type == "movement_speed" and value > rules["max_movement_bonus"]:
                return {
                    "accepted": False,
                    "reason": "movement_bonus_too_high",
                }
            if effect_type == "attack_speed" and value > rules["max_attack_speed"]:
                return {
                    "accepted": False,
                    "reason": "attack_speed_too_high",
                }
            if effect_type == "crit" and value > rules["max_crit"]:
                return {
                    "accepted": False,
                    "reason": "crit_too_high",
                }
            if effect_type == "stun" and value > rules["max_stun_duration"]:
                return {
                    "accepted": False,
                    "reason": "stun_duration_too_high",
                }

        return {
            "accepted": True,
            "reason": "ok",
        }

    def validate_progression_rules(item_def):
        required_rank = item_def.get("acquisition", {}).get("required_rank", "D")
        if required_rank in ("S", "A") and store.guild_rank not in ("S", "A"):
            return {
                "accepted": True,
                "availability": "locked",
                "reason": "rank_locked",
            }

        return {
            "accepted": True,
            "availability": "available",
            "reason": "ok",
        }

    def validate_item_proposal(item_def):
        if ITEM_PROPOSAL_FORBIDDEN_FIELDS.intersection(item_def.keys()):
            return {
                "accepted": False,
                "reason": "forbidden_ai_state_field",
                "power": 0,
                "budget": 0,
            }

        acquisition = item_def.get("acquisition", {})
        if ITEM_PROPOSAL_FORBIDDEN_FIELDS.intersection(acquisition.keys()):
            return {
                "accepted": False,
                "reason": "forbidden_ai_acquisition_field",
                "power": 0,
                "budget": 0,
            }

        balance = validate_item_balance(item_def)
        if not balance["accepted"]:
            return balance

        world = validate_world_rules(item_def)
        if not world["accepted"]:
            world["power"] = balance.get("power", 0)
            world["budget"] = balance.get("budget", 0)
            return world

        progression = validate_progression_rules(item_def)
        progression["power"] = balance.get("power", 0)
        progression["budget"] = balance.get("budget", 0)
        return progression
