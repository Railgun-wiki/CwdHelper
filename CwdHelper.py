# -*- coding: utf-8 -*-

import os

HelpMessage = '''---MCDR-Cwd-Helper---By-Railgun_ALGO
§a食用方法:§7!!cwd §6[-Commend]§r
§a【例子】§r
§7!!cwd §6sudo reboot §r重启服务器
'''

PLUGIN_METADATA = {
    'id': 'cwd_helper',
    'version': '1.0.0',
    'name': 'CwdHelper',
    'description': 'Use command "!!cwd" to send commend to the system',
    'author': [
        'Railgun_ALGO',  # The author of this plugin
        'Fallen_Breath'  # The author of MCDReforged
    ],
    'link': 'https://github.com/Railgun-wiki/CwdHelper',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}


def on_info(server, info):
    if info.is_player:
        if info.content.startswith('!!cwd'):
            WCwd = info.content[6:]
            if len(WCwd) == 0:
                server.tell(info.player, HelpMessage)
            else:
                output = os.popen(WCwd)
                Cwd_info = output.readlines()
                for line in Cwd_info:
                    server.tell(info.player, line.strip('\r\n'))


def on_load(server, prev):
    server.register_help_message('!!cwd', 'Send commend to the system')
