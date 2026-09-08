default childhood_month_index = 0
default childhood_complete = False

init python:
    CHILDHOOD_START_AGE = 6
    CHILDHOOD_END_AGE = 12

    def reset_time_state():
        store.player_age = CHILDHOOD_START_AGE
        store.player_month = 1
        store.childhood_month_index = 0
        store.childhood_complete = False

    def get_time_label():
        return "Tuổi %s - Tháng %s" % (store.player_age, store.player_month)

    def advance_month():
        if store.childhood_complete:
            return {
                "age": store.player_age,
                "month": store.player_month,
                "completed": True,
            }

        store.childhood_month_index += 1
        store.player_month += 1

        if store.player_month > 12:
            store.player_month = 1
            store.player_age += 1

        if store.player_age >= CHILDHOOD_END_AGE:
            store.player_age = CHILDHOOD_END_AGE
            store.player_month = 1
            store.childhood_complete = True

        return {
            "age": store.player_age,
            "month": store.player_month,
            "completed": store.childhood_complete,
        }

    def set_age(age):
        store.player_age = age
        if store.player_age >= CHILDHOOD_END_AGE:
            store.childhood_complete = True

    def set_month(month):
        store.player_month = max(1, min(12, month))
