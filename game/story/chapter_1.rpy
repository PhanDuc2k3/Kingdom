label chapter_1_intro:
    $ story_chapter = 1
    $ set_story_stage("chapter_1_start", "bedroom", 0)

    scene black
    with fade

    centered "{size=64}CHƯƠNG I{/size}\n\n{size=42}NGƯỜI THỪA KẾ VÙNG BIÊN{/size}"

    scene bg border_day
    with fade

    narrator "Bên ngoài cửa sổ là một vùng đất mà ta chưa từng biết."
    narrator "Những ngọn núi."
    narrator "Những cánh rừng."
    narrator "Những ngôi làng nhỏ nằm dưới chân thành."
    narrator "Và tất cả chúng..."
    narrator "...một ngày nào đó sẽ trở thành trách nhiệm của ta."

    jump chapter_1_start


label chapter_1_start:
    narrator "Bản dựng hiện tại dừng tại điểm bắt đầu Chương I."
    return
