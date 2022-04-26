from libqtile import widget
from libqtile.config import Screen
from libqtile import widget, bar

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    background = '#ff9500'
                ),

                widget.Sep(
                    background = '#73a832'
                ),

                widget.WindowName(
                    background = '#00ff6a'
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
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
