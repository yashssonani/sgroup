#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

import os


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


from plugins.display_progress import progress_for_pyrogram, humanbytes
from plugins.youtube_dl_button import youtube_dl_call_back


async def button(bot, update):
    # LOGGER.info(update)
    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
