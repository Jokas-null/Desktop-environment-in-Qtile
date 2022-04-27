from libqtile import widget
from libqtile.config import Screen
from libqtile import widget, bar

def separator():
    return widget.Sep(
        background = '#321450',
        linewidth = 0,
        padding = 5
    )

def left_box_decoration(color):
    return widget.TextBox(
        "", #nf-ple-left_half_circle_thick
        width=10,
        fontsize = 40,
        foreground = color,
        padding = 3
    )

def right_box_decoration(color):
    return widget.TextBox(
        "", #nf-ple-right_half_circle_thick
        width=10,
        fontsize = 30,
        foreground = color,
        padding = -7
    )

def icon(icon,color):
    return widget.TextBox(
        icon,
        background = color,
        fontsize = 20
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active = '#b000ff',
                    inactive = '#ff0677',
                    fontsize = 16,
                    highlight_method='line',
                    highlight_color = '#ffcadc',
                    block_highlight_text_color = '#0051ff',
                    borderwidth = 0,
                    center_aligned = True,
                    spacing = 0,
                ),
                separator(),
                left_box_decoration("#633450"),
                widget.WindowName(
                    background = '#633450',
                    padding = 5,
                    foreground = '#bd00ff'
                ),
                right_box_decoration("#633450"),
                separator(),
                left_box_decoration("#001eff"),
                icon("","#001eff"),
                widget.CheckUpdates(
                    background = '#001eff',
                    colour_have_updates = '#cfc100',
                    colour_no_updates = '#fe75fe',
                    fontsize = 13,
                    display_format = 'Updates: {updates}',
                    no_update_string = ' 0',
                    update_interval = 1800,
                    distro = 'Arch',
                    custom_command='checkupdates',
                ),
                right_box_decoration("#001eff"),
                separator(),              
                left_box_decoration("#00ff9f"),
                icon('龍 ','#00ff9f'),
                widget.Net(
                    background = '#00ff9f',
                    interface='ens33',
                    format = '{down}   {up}'
                ),
                right_box_decoration("#00ff9f"),
                widget.Systray(
                    padding = 5
                ),
                separator(),
                left_box_decoration("#7a04eb"),
                icon(" ","#7a04eb"),
                widget.CPUGraph(
                    type = 'box',
                    background = '#7a04eb',
                    border_color = '#7a04eb',
                    graph_color = '#fe75fe'
                ),
                right_box_decoration("#7a04eb"),
                separator(),
                left_box_decoration("#fd00ff"),
                icon(" ","#fd00ff"),
                widget.CurrentLayout(
                    background = '#fd00ff',
                    foreground = '#efe492',
                ),
                right_box_decoration("#fd00ff"),
                separator(),
                left_box_decoration("#ff0677"),
                icon(" ","#ff0677"),
                 widget.Clock(format="%d/%m/%Y - %H:%M",
                    background = '#ff0677',
                    foreground = '#efe492'
                ),
                right_box_decoration("#ff0677"),
            ],
            30,
            background = '#321450'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

widget_defaults = dict(
    font="Caskaydia Cove Nerd Font",
    fontsize=13,
    padding=1,
)
extension_defaults = widget_defaults.copy()
