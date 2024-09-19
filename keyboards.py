from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButtonPollType

# Define the main keyboard
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Maqola"), KeyboardButton(text="Tezis")],
        [KeyboardButton(text="Dissertatsiyalar"), KeyboardButton(text="Doktrskiy")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,  # Optional: Makes the keyboard disappear after one use
    input_field_placeholder="Menyuni tanlang"
)

# Inline keyboard for links
links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Maqolalar", url="https://www.gazeta.uz/oz/list/articles/"),
            InlineKeyboardButton(text="Articles", url="https://www.nature.com/nature/articles"),
        ]
    ]
)

# Specialty keyboard with additional options
spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ma'lumotlar", request_location=True),
            KeyboardButton(text="Telefon Nomeri", request_contact=True),
            KeyboardButton(text="Savol", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)

# Inline keyboard for thesis links
tezis_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tezis", url="https://www.bing.com/search?pglt=2083&q=tezislar&cvid=11da994b47294abf9ae014a562464ae3&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDY1MzFqMGoxqAIIsAIB&FORM=ANNTA1&PC=EDGEDSE"),
            InlineKeyboardButton(text="Thesis", url="https://typeset.io/resources/what-is-a-thesis-a-complete-guide/")
        ]
    ]
)
