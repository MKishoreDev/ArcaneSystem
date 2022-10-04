from pyrogram.types import InlineKeyboardButton

START_BUTTON = [
    [
        InlineKeyboardButton("𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/playBoysDXD"),
        InlineKeyboardButton("𝗦𝗽𝗮𝗺 𝗥𝗲𝗽𝗼𝗿𝘁", url="https://t.me/playBoysDXD"),
    ],
    [
        InlineKeyboardButton("𝗛𝗲𝗹𝗽 𝗚𝘂𝗶𝗱𝗲𝗹𝗶𝗻𝗲𝘀", callback_data="back_help"),   
    ],   
    [
        InlineKeyboardButton("𝗥𝘂𝗹𝗲𝘀", callback_data="Rules"),   
    ],   
]

HELP_BUTTON = [
        [
            InlineKeyboardButton("𝗦𝗰𝗮𝗻", callback_data="scan_help"),
            InlineKeyboardButton("𝗘𝘅𝘁𝗿𝗮", callback_data="extra"),
        ],
        [
            InlineKeyboardButton("𝗕𝗮𝗻-𝗖𝗼𝗱𝗲𝘀", callback_data="bancodes"),
            InlineKeyboardButton("𝗖𝗹𝗼𝘀𝗲", callback_data="delete"),
    ],   
]

SCANHELP_BUTTON = [
        [
            InlineKeyboardButton("𝗦𝗰𝗮𝗻", callback_data="scan_help"),
            InlineKeyboardButton("𝗘𝘅𝘁𝗿𝗮", callback_data="extra"),
        ],
        [
            InlineKeyboardButton("𝗕𝗮𝗻-𝗖𝗼𝗱𝗲𝘀", callback_data="bancodes_help"),
            InlineKeyboardButton("𝗕𝗮𝗰𝗸", callback_data="back_help"),
    ],   
]

SCANHELP_BUTTON2 = [
        [
            InlineKeyboardButton("𝗦𝗰𝗮𝗻", callback_data="scan_help"),
            InlineKeyboardButton("𝗘𝘅𝘁𝗿𝗮", callback_data="extra"),
        ],
        [
            InlineKeyboardButton("𝗕𝗮𝗻-𝗖𝗼𝗱𝗲𝘀", callback_data="bancodes_help"),
            InlineKeyboardButton("𝗖𝗹𝗼𝘀𝗲", callback_data="delete"),
    ],   
]

SCANHELP_BUTTON3 = [
        [
            InlineKeyboardButton("𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/playBoysDXD"),
            InlineKeyboardButton("𝗦𝗽𝗮𝗺 𝗥𝗲𝗽𝗼𝗿𝘁", url="https://t.me/playBoysDXD"),
        ],
        [
            InlineKeyboardButton("𝗛𝗲𝗹𝗽 𝗚𝘂𝗶𝗱𝗲𝗹𝗶𝗻𝗲𝘀", callback_data="back_help"),
    ],   
]

RULES_BUTTON = [
        [
            InlineKeyboardButton("𝗜𝗻𝘀𝗽𝗲𝗰𝘁𝗼𝗿 𝗥𝘂𝗹𝗲𝘀", callback_data="basic_scanner_rules"),
            InlineKeyboardButton("𝗛𝘂𝗺𝗮𝗻 𝗥𝘂𝗹𝗲𝘀", callback_data="Girls_Safe_Rule"),
        ],
        [
            InlineKeyboardButton("𝗧𝗼𝘅𝗶𝗰 𝗥𝘂𝗹𝗲𝘀", callback_data="Toxic_Boom"),
            InlineKeyboardButton("𝗚𝗿𝗼𝘂𝗽 𝗥𝘂𝗹𝗲𝘀", callback_data="group_rules"),
        ],
        [
            InlineKeyboardButton("𝗖𝗹𝗼𝘀𝗲", callback_data="delete"),
    ],   
]

RULES_BUTTON2 = [
        [
            InlineKeyboardButton("𝗜𝗻𝘀𝗽𝗲𝗰𝘁𝗼𝗿 𝗥𝘂𝗹𝗲𝘀", callback_data="basic_scanner_rules"),
            InlineKeyboardButton("𝗛𝘂𝗺𝗮𝗻 𝗥𝘂𝗹𝗲𝘀", callback_data="Girls_Safe_Rule"),
        ],
        [
            InlineKeyboardButton("𝗧𝗼𝘅𝗶𝗰 𝗥𝘂𝗹𝗲𝘀", callback_data="Toxic_Boom"),
            InlineKeyboardButton("𝗚𝗿𝗼𝘂𝗽 𝗥𝘂𝗹𝗲𝘀", callback_data="group_rules"),
        ],
        [
            InlineKeyboardButton("𝗕𝗮𝗰𝗸", callback_data="Rules"),
    ],   
]
