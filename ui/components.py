import customtkinter as ctk

from assets.theme.theme import *


class BotaoPrimario(ctk.CTkButton):

    def __init__(self, master, text, command=None, width=330):

        super().__init__(
            master,

            text=text,

            command=command,

            width=width,

            height=48,

            corner_radius=RADIUS,

            fg_color=PRIMARY,

            hover_color=PRIMARY_HOVER,

            text_color=TEXT,

            font=FONT_TEXT
        )