label event_first_sword_training:
    scene bg training_courtyard
    with dissolve
    narrator "Giáo quan đặt thanh kiếm gỗ vào đôi tay nhỏ của bạn, rồi im lặng chờ bạn tự tìm lại thăng bằng."
    narrator "Nó nặng hơn một món đồ chơi, nhẹ hơn một thanh kiếm thật, và thành thật hơn rất nhiều lời nói trong dinh thự."
    $ complete_event("event_first_sword_training")
    return

label event_first_magic_study:
    scene bg magic_study_room
    with dissolve
    narrator "Một ngọn nến được đặt trước mặt bạn. Giáo sư ma pháp bảo bạn đừng ra lệnh cho ngọn lửa, chỉ cần lắng nghe nó."
    narrator "Trong một nhịp tim rất khẽ, thứ gì đó bên trong bạn đáp lại bằng hơi ấm mờ nhạt."
    $ complete_event("event_first_magic_study")
    return

label event_sword_milestone_5:
    scene bg training_courtyard
    with dissolve
    narrator "Thế thủ của bạn đã sạch hơn. Giáo quan không còn phải sửa cổ tay bạn sau mỗi vài nhịp thở."
    $ complete_event("event_sword_milestone_5")
    return

label event_sword_milestone_10:
    scene bg mansion_main_hall
    with dissolve
    narrator "Sau bữa tối, giáo quan báo cáo tiến bộ của bạn trong đại sảnh."
    scene bg training_courtyard
    with dissolve
    narrator "Bạn vẫn chưa được phép luyện với kiếm thép, nhưng thanh kiếm gỗ trong tay bạn đã bắt đầu có ý đồ rõ ràng."
    $ complete_event("event_sword_milestone_10")
    return

label event_first_class_swordsman:
    scene bg training_courtyard
    with dissolve
    narrator "Giáo quan quan sát tư thế của bạn, rồi hiếm hoi gật đầu."
    narrator "Bạn đã có nền tảng của một Kiếm sĩ."
    $ unlock_class("swordsman")
    $ complete_event("event_first_class_swordsman")
    return

label event_first_class_mage:
    scene bg magic_study_room
    with dissolve
    narrator "Ngọn nến nghiêng về phía lòng bàn tay bạn mà không làm bỏng da."
    narrator "Mana của bạn đã có hình dạng đầu tiên, đủ để được gọi là bước khởi đầu của một Pháp sư."
    $ unlock_class("mage")
    $ complete_event("event_first_class_mage")
    return

label event_magic_swordsman_discovery:
    scene bg training_courtyard
    with dissolve
    narrator "Trong lúc luyện kiếm, bản năng khiến bạn dẫn một luồng mana mỏng chạy dọc theo lưỡi kiếm gỗ."
    narrator "Chỉ trong một nhát vung sạch sẽ, kiếm và pháp thuật đáp lại nhau như thể chúng vốn thuộc cùng một hơi thở."
    $ unlock_class("magic_swordsman")
    $ complete_event("event_magic_swordsman_discovery")
    return

label event_secret_hallway:
    scene bg mansion_corridor
    with dissolve
    narrator "Sau một tấm thảm treo tường đã phai màu, bạn tìm thấy hành lang hẹp dành cho người hầu, gần như đã bị khách khứa lãng quên."
    $ set_world_flag("secret_hallway_found")
    $ complete_event("event_secret_hallway")
    return

label event_old_history_book:
    scene bg mansion_library
    with dissolve
    narrator "Một cuốn biên niên sử vùng biên cũ nhắc đến nạn đói, quái vật tràn ra và tranh chấp quý tộc lặp lại theo những chu kỳ đáng ngại."
    $ set_world_flag("old_border_history_read")
    $ complete_event("event_old_history_book")
    return

label event_instructor_praise:
    scene bg training_courtyard
    with dissolve
    narrator "Giáo quan kiếm thuật không mỉm cười, nhưng lần sửa lỗi tiếp theo của ông nhẹ hơn thường lệ."
    $ adjust_relationship("sword_instructor", "respect", 2)
    $ complete_event("event_instructor_praise")
    return

label event_archery_first_mark:
    scene bg archery_range
    with dissolve
    narrator "Một mũi tên của bạn cuối cùng cũng cắm gần tâm bia."
    narrator "Không ai hô lên. Nhưng người giữ sân tập lặng lẽ đổi bia mới, như thể kết quả đó đáng được ghi nhận."
    $ set_world_flag("first_clean_archery_mark")
    $ complete_event("event_archery_first_mark")
    return

label event_healing_servant_cut:
    scene bg divine_ceremony_hall
    with dissolve
    narrator "Một cô hầu làm đứt tay trong lúc chuẩn bị đồ lễ. Vết thương nhỏ, nhưng máu khiến cô luống cuống."
    narrator "Bạn không chữa lành nó bằng phép màu. Bạn rửa sạch, băng lại, rồi giúp cô bình tĩnh thở đều."
    $ set_world_flag("helped_injured_servant")
    $ adjust_relationship("maid", "trust", 2)
    $ complete_event("event_healing_servant_cut")
    return

label event_mother_old_letter:
    scene bg mother_room
    with dissolve
    narrator "Mẹ cho bạn xem một lá thư cũ, nét chữ đã nhạt nhưng vẫn được giữ rất cẩn thận."
    narrator "Bà không kể hết câu chuyện phía sau nó. Nhưng lần đầu tiên, bạn thấy nỗi lo trong mắt mẹ không chỉ dành cho riêng bạn."
    $ set_world_flag("mother_shared_old_letter")
    $ adjust_relationship("mother", "affection", 2)
    $ complete_event("event_mother_old_letter")
    return

label event_father_border_map:
    scene bg war_room
    with dissolve
    narrator "Cha đứng trước bản đồ vùng biên rất lâu. Những ghim đỏ dày hơn hẳn ở phía bắc."
    narrator "Ông không giải thích nhiều, nhưng khi bạn chỉ ra một tuyến đường vòng qua rừng, ánh mắt ông dừng lại trên bạn thêm một nhịp."
    $ set_world_flag("noticed_border_route")
    $ adjust_relationship("father", "affection", 1)
    $ complete_event("event_father_border_map")
    return

label event_tax_ledger_shortage:
    scene bg father_study
    with dissolve
    narrator "Trong sổ thuế, bạn phát hiện một khoản hụt nhỏ lặp lại ở cùng một tuyến vận chuyển."
    narrator "Có thể chỉ là sai sót. Cũng có thể là dấu vết của một bàn tay rất quen việc."
    $ set_world_flag("noticed_tax_shortage")
    $ complete_event("event_tax_ledger_shortage")
    return

label event_garden_servant_rumor:
    scene bg mansion_garden
    with dissolve
    narrator "Trong lúc nghỉ dưới giàn cây, bạn nghe hai người hầu nhắc tới đoàn người tị nạn vừa bị chặn ngoài thị trấn."
    narrator "Họ ngừng nói khi thấy bạn. Nhưng lời đó đã ở lại."
    $ set_world_flag("saw_refugees_rumor")
    $ complete_event("event_garden_servant_rumor")
    return

label event_library_locked_shelf:
    scene bg mansion_library
    with dissolve
    narrator "Ở cuối thư viện có một kệ sách bị khóa, trên gáy tủ khắc huy hiệu cũ của gia tộc."
    narrator "Bạn chưa mở được nó, nhưng giờ bạn biết có những ghi chép trong dinh thự không dành cho trẻ con."
    $ set_world_flag("found_locked_library_shelf")
    $ complete_event("event_library_locked_shelf")
    return

label event_mansion_guest_adventurer:
    scene bg mansion_main_hall
    with dissolve
    narrator "Một vị khách mặc áo choàng bụi đường được quản gia dẫn qua đại sảnh."
    narrator "Trên thắt lưng ông ta có một huy hiệu lạ: thanh kiếm đặt trước cánh cổng mở."
    $ set_world_flag("saw_adventurer_badge")
    $ complete_event("event_mansion_guest_adventurer")
    return

label event_sneak_out:
    scene bg mansion_back_gate_night
    with dissolve
    narrator "Một cổng phụ vẫn chưa được cài then sau hoàng hôn. Bên kia là mùi khói, bùn đất và tiếng ồn mơ hồ của thị trấn."
    menu:
        "Bạn làm gì?"
        "Quay lại trước khi có ai nhận ra.":
            narrator "Bạn lùi vào trong dinh thự, giữ bí mật này cho riêng mình."
            $ set_world_flag("found_service_gate")
        "Lẻn ra ngoài nhìn một lát.":
            scene bg border_town_street
            with dissolve
            narrator "Bạn thấy những đứa trẻ đói bên vệ đường, lính gác mệt mỏi ở cổng phố và một huy hiệu mạo hiểm giả trên áo choàng của khách lữ hành."
            scene bg border_town_market
            with dissolve
            narrator "Qua những sạp hàng, một huy hiệu của Hội Mạo Hiểm Giả treo xa phía cuối quảng trường, nửa khuất trong khói đuốc."
            $ set_world_flag("sneaked_out_once")
            $ set_world_flag("knows_adventurer_guild")
    $ complete_event("event_sneak_out")
    return

label event_political_warning:
    scene bg family_dining_room
    with dissolve
    narrator "Bữa tối kết thúc sớm khi một người đưa tin đến trước bàn ăn gia đình."
    scene bg war_room
    with dissolve
    narrator "Một lá thư niêm sáp đen được đưa vào phòng làm việc của cha."
    narrator "Đến tối, cả dinh thự đều nói nhỏ hơn thường lệ. Cướp đường, quái vật, binh lính thiếu lương và quý tộc bất phục tùng xuất hiện trong cùng một bầu không khí nặng nề."
    $ set_world_flag("heard_noble_rebellion")
    $ complete_event("event_political_warning")
    return

label chapter_1_age_11_final_event:
    scene bg mansion_exterior_day
    with fade
    narrator "Gần cuối năm mười một tuổi của bạn, một hiệp sĩ bị thương trở về dinh thự trước bình minh."
    scene bg war_room
    with dissolve
    narrator "Một pháo đài biên giới đã mất liên lạc. Cha bạn ra lệnh chuẩn bị bản đồ, ngựa và người đưa tin trước cả bữa sáng."
    narrator "Thế giới bên ngoài dinh thự không còn là lời đồn ở rìa cuộc trò chuyện của người lớn nữa."
    $ set_world_flag("age_11_border_crisis")
    $ build_childhood_summary()
    call screen childhood_summary_screen
    jump chapter_2_age_12_hook

label chapter_2_age_12_hook:
    $ set_story_stage("age_12_hook", "earls_mansion", 0)
    narrator "Tuổi 12 bắt đầu tại đây. Chương tiếp theo có thể đọc lại tuổi thơ, Thần Tâm, chức nghiệp, quan hệ và các flag bạn đã tạo."
    return
