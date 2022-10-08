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

UNSCAN_BUTTON = [[ InlineKeyboardButton(text="revert", callback_data="bunscan")]]

RESCAN_BUTTON = [[ InlineKeyboardButton(text="Scan", callback_data="bscan")]]

STATUS_BUTTON = [
    [
        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/HangOverXD"),
        InlineKeyboardButton("Sᴘᴀᴍ ʀᴇᴘᴏʀᴛ", url="https://t.me/HangOverXD"),   
    ],
]

ADD_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("﹀", callback_data="EXTRA_DEMOTEE"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

EXTRA_DEMOTE = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Eɴғᴏʀᴄᴇʀ", callback_data="RMENF"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴsᴘᴇᴄᴛᴏʀ", callback_data="RMINS"),
        ],
        [
            InlineKeyboardButton("︿", callback_data="ADDD_BUTTON"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

# Extra 

INSED_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs 🔘", callback_data="ADDINS"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("﹀", callback_data="EXTRA_DEMOTEE"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

ENFED_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ 🔘", callback_data="ADDENF"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("﹀", callback_data="EXTRA_DEMOTEE"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

I_TO_E_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ 🔘", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("﹀", callback_data="EXTRA_DEMOTEE"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

E_TO_I_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs 🔘", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("﹀", callback_data="EXTRA_DEMOTEE"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

RMENFED_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Eɴғᴏʀᴄᴇʀ 🔘", callback_data="RMENF"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴsᴘᴇᴄᴛᴏʀ", callback_data="RMINS"),
        ],
        [
            InlineKeyboardButton("︿", callback_data="ADDD_BUTTON"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

RMINSED_BUTTON = [
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Eɴғ", callback_data="ADDENF"),
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Tᴏ Iɴs", callback_data="ADDINS"),
        ],
        [
            InlineKeyboardButton("Pʀᴏᴍᴏᴛᴇ Eɴғ Tᴏ Iɴs", callback_data="E_TO_I"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴs Tᴏ Eɴғ", callback_data="I_TO_E"),
        ],
        [
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Eɴғᴏʀᴄᴇʀ", callback_data="RMENF"),
            InlineKeyboardButton("Dᴇᴍᴏᴛᴇ Iɴsᴘᴇᴄᴛᴏʀ 🔘", callback_data="RMINS"),
        ],
        [
            InlineKeyboardButton("︿", callback_data="ADDD_BUTTON"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="Delete"),
    ],   
]

