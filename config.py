import subprocess, os
from libqtile import hook
from settings.layouts import layouts, floating_layout
from settings.keys import mod, keys
from settings.groups import groups
from settings.mouse import mouse
from settings.widgets import widget_defaults ,extension_defaults, screens

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

dgroups_key_binder = None
dgroups_app_rules = [] 
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"