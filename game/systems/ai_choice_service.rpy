default current_ai_choices = []
default last_ai_response = {}
default ai_service_failed = False

init python:
    CHOICE_CATEGORIES = (
        "intelligence",
        "observation",
        "social",
        "deception",
        "kindness",
        "bold",
        "noble",
        "combat",
        "survival",
    )

    CHOICE_CATEGORY_LABELS = {
        "intelligence": "Trí tuệ",
        "observation": "Quan sát",
        "social": "Giao tiếp",
        "deception": "Đánh lừa",
        "kindness": "Dịu dàng",
        "bold": "Quyết đoán",
        "noble": "Phong thái quý tộc",
        "combat": "Chiến đấu",
        "survival": "Sinh tồn",
    }

    def get_choice_category_label(category):
        return CHOICE_CATEGORY_LABELS.get(category, category)

    DANGEROUS_AI_FIELDS = {
        "story_stage",
        "next_stage",
        "stat",
        "stats",
        "relationship",
        "relationships",
        "inventory",
        "death",
        "kill",
        "teleport",
        "quest_complete",
        "gold",
        "hp",
        "stamina",
    }

    NPC_PERSONALITIES = {
        "mother": [
            "dịu dàng",
            "che chở",
            "thanh nhã",
            "thông minh",
            "yêu thương con sâu sắc",
        ],
        "father": [
            "nghiêm khắc",
            "kỷ luật",
            "tư duy quân sự",
            "có trách nhiệm",
            "yêu gia đình nhưng hiếm khi bộc lộ cảm xúc",
        ],
        "butler": [
            "điềm tĩnh",
            "chuẩn mực",
            "rất tinh ý",
            "trung thành",
            "giàu kinh nghiệm",
        ],
    }

    def fallback_ai_choices():
        return [
            {
                "id": "observe_surroundings",
                "text": "Quan sát xung quanh.",
                "category": "observation",
            },
            {
                "id": "ask_what_happened",
                "text": "Hỏi chuyện gì đã xảy ra.",
                "category": "intelligence",
            },
            {
                "id": "stay_silent",
                "text": "Im lặng.",
                "category": "observation",
            },
            {
                "id": "speak_gently",
                "text": "Nói chuyện nhẹ nhàng.",
                "category": "kindness",
            },
        ]

    def build_ai_context(npc_id, allowed_actions=None):
        return {
            "story_stage": store.story_stage,
            "location": store.current_location,
            "player_age": store.player_age,
            "npc": {
                "id": npc_id,
                "personality": NPC_PERSONALITIES.get(npc_id, []),
            },
            "recent_dialogue": list(store.recent_dialogue),
            "allowed_actions": allowed_actions or [
                "đặt câu hỏi",
                "quan sát",
                "nói dối",
                "im lặng",
                "tương tác với nhân vật hiện tại",
            ],
            "forbidden_actions": [
                "rời khỏi dinh thự",
                "giết nhân vật quan trọng",
                "bỏ qua thời gian",
                "thay đổi cốt truyện chính",
                "thay đổi chỉ số trực tiếp",
                "thay đổi quan hệ trực tiếp",
            ],
            "world_context": "Nhân vật chính là người thừa kế quý tộc sáu tuổi vừa chuyển sinh tại một lãnh địa biên giới đang gặp khó khăn.",
        }

    def validate_ai_choices(response):
        try:
            if not isinstance(response, dict):
                raise ValueError("AI response must be a dictionary.")

            if DANGEROUS_AI_FIELDS.intersection(response.keys()):
                raise ValueError("AI response contains forbidden top-level fields.")

            raw_choices = response.get("choices", [])
            if not isinstance(raw_choices, list):
                raise ValueError("AI choices must be a list.")

            valid_choices = []

            for item in raw_choices[:4]:
                if not isinstance(item, dict):
                    continue

                if DANGEROUS_AI_FIELDS.intersection(item.keys()):
                    continue

                choice_id = item.get("id", "")
                text = item.get("text", "")
                category = item.get("category", "")

                if not isinstance(choice_id, str) or not choice_id.strip():
                    continue
                if not isinstance(text, str) or not text.strip():
                    continue
                if category not in CHOICE_CATEGORIES:
                    continue

                valid_choices.append({
                    "id": choice_id.strip(),
                    "text": text.strip(),
                    "category": category,
                })

            if not valid_choices:
                raise ValueError("AI response contains no valid choices.")

            store.ai_service_failed = False
            return valid_choices

        except Exception:
            store.ai_service_failed = True
            return fallback_ai_choices()

    def request_ai_choices(context):
        stage = context.get("story_stage")
        npc_id = context.get("npc", {}).get("id")

        if stage == "mother_conversation" and npc_id == "mother":
            return {
                "narration": "Người phụ nữ nhìn cậu bằng ánh mắt vừa mừng vừa lo.",
                "speaker": "mother",
                "dialogue": "Con thật sự tỉnh rồi sao?",
                "choices": [
                    {
                        "id": "ask_what_happened",
                        "text": "Hỏi chuyện gì đã xảy ra.",
                        "category": "intelligence",
                    },
                    {
                        "id": "observe_mother",
                        "text": "Không nói gì, quan sát căn phòng và người phụ nữ trước mặt.",
                        "category": "observation",
                    },
                    {
                        "id": "pretend_amnesia",
                        "text": "Giả vờ không nhớ bà là ai.",
                        "category": "deception",
                    },
                    {
                        "id": "call_mother",
                        "text": "Khẽ gọi bà là mẹ.",
                        "category": "kindness",
                    },
                ],
            }

        if stage == "father_arrival" and npc_id == "father":
            return {
                "narration": "Người đàn ông đứng bên giường, giọng trầm và kiềm chế.",
                "speaker": "father",
                "dialogue": "Con còn đau ở đâu không?",
                "choices": [
                    {
                        "id": "answer_calmly",
                        "text": "Bình tĩnh trả lời rằng mình đã ổn.",
                        "category": "noble",
                    },
                    {
                        "id": "study_father",
                        "text": "Quan sát thái độ của cha trước khi trả lời.",
                        "category": "observation",
                    },
                    {
                        "id": "ask_father_status",
                        "text": "Hỏi cha đã xảy ra chuyện gì.",
                        "category": "intelligence",
                    },
                ],
            }

        return {
            "choices": fallback_ai_choices()
        }

    def prepare_ai_choices(npc_id, allowed_actions=None):
        context = build_ai_context(npc_id, allowed_actions)
        store.last_ai_response = request_ai_choices(context)
        store.current_ai_choices = validate_ai_choices(store.last_ai_response)
        return store.current_ai_choices
