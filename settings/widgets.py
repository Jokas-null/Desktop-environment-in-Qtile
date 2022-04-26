from libqtile import widget
from libqtile.config import Screen
from libqtile import widget, bar

def separator():
    return widget.Sep(
        background = '#73a832',
        linewidth = 0,
        padding = 6
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    #background = '#ff9500'
                    active = '#bd8a13',
                    highlight_method='block',
                    borderwidth = 3,
                    center_aligned =  True
                ),

                separator(),

                widget.WindowName(
                    #background = '#00ff6a'
                ),
                widget.Systray(),
                widget.CPUGraph(
                    type = 'box',
                    background = '#000000',
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",
                    background = '#692566' 
                ),
                widget.CurrentLayout(
                    background = '#5d7591',
                    fontshadow = '#2f3338',
                    foreground = '#2f3833',
                ),
                widget.QuickExit(),
            ],
            30,
            background = '#5e13cf'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()
