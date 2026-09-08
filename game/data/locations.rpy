init python:
    LOCATION_DEFINITIONS = {
        "main_bedroom": {"name": "Phòng ngủ của Main", "bg": "bg main_bedroom_day"},
        "mansion_main_hall": {"name": "Đại sảnh dinh thự", "bg": "bg mansion_main_hall"},
        "mansion_corridor": {"name": "Hành lang dinh thự", "bg": "bg mansion_corridor"},
        "mansion_library": {"name": "Thư viện", "bg": "bg mansion_library"},
        "training_courtyard": {"name": "Sân luyện kiếm", "bg": "bg training_courtyard"},
        "magic_study_room": {"name": "Phòng học ma pháp", "bg": "bg magic_study_room"},
        "archery_range": {"name": "Khu luyện cung", "bg": "bg archery_range"},
        "father_study": {"name": "Phòng làm việc của Bá tước", "bg": "bg father_study"},
        "mother_room": {"name": "Phòng của mẹ", "bg": "bg mother_room"},
        "mansion_garden": {"name": "Vườn dinh thự", "bg": "bg mansion_garden"},
        "family_dining_room": {"name": "Phòng ăn gia đình", "bg": "bg family_dining_room"},
        "mansion_exterior_day": {"name": "Mặt ngoài dinh thự", "bg": "bg mansion_exterior_day"},
        "divine_ceremony_hall": {"name": "Đại điện nghi lễ", "bg": "bg divine_ceremony_hall"},
        "divine_realm": {"name": "Thần giới", "bg": "bg divine_realm"},
        "mansion_back_gate_night": {"name": "Cổng phụ sau dinh thự", "bg": "bg mansion_back_gate_night"},
        "border_town_street": {"name": "Đường phố thị trấn vùng biên", "bg": "bg border_town_street"},
        "border_town_market": {"name": "Khu chợ vùng biên", "bg": "bg border_town_market"},
        "war_room": {"name": "Phòng họp chiến sự", "bg": "bg war_room"},
    }

    def set_location(location_id):
        location = LOCATION_DEFINITIONS.get(location_id)
        if not location:
            return False
        store.current_location = location.get("name", location_id)
        set_location_bg(location.get("bg"))
        return True
