from libqtile import widget
from libqtile.config import Screen
from libqtile import widget, bar

def separator():
    return widget.Sep(
        background = '#333333',
        linewidth = 0,
        padding = 5
    )

def left_box_decoration(color):
    return widget.TextBox(
        "", #nf-ple-left_half_circle_thick
        width=15,
        fontsize = 40,
        foreground = color,
        padding = 3
    )

def right_box_decoration(color):
    return widget.TextBox(
        "", #nf-ple-right_half_circle_thick
        width=10,
        heigh=10,
        fontsize = 35,
        foreground = color,
        padding = -10
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
                    active = '#99FF66',
                    inactive = '#009900',
                    fontsize = 20,
                    highlight_method='line',
                    highlight_color = '#FFFFCC',
                    block_highlight_text_color = '#FF0000',
                    borderwidth = 0,
                    center_aligned = True,
                    spacing = 5,
                ),
                separator(),
                left_box_decoration("#666666"),
                widget.WindowName(
                    background = '#666666',
                    padding = 5,
                    foreground = '#000000',
                    fontsize=15,
                ),
                right_box_decoration("#666666"),
                separator(),
                #left_box_decoration("#001eff"),
                #icon("","#001eff"),
                #widget.CheckUpdates(
                #    background = '#001eff',
                #    colour_have_updates = '#cfc100',
                #    colour_no_updates = '#fe75fe',
                #    fontsize = 13,
                #    display_format = 'Updates: {updates}',
                #    no_update_string = ' 0',
                #    update_interval = 1800,
                #    distro = 'Arch',
                #    custom_command='checkupdates',
                #),
                #right_box_decoration("#001eff"),
                separator(),
                left_box_decoration("#009900"),
                icon('龍 ','#009900'),
                widget.Net(
                    background = '#009900',
                    interface='enp0s3',
                    format = '{down}   {up}'
                ),
                right_box_decoration("#009900"),
                widget.Systray(
                    padding = 5
                ),
                separator(),
                left_box_decoration("#000000"),
                icon(" ","#000000"),
                widget.CPUGraph(
                    type = 'box',
                    background = '#000000',
                    border_color = '#000000',
                    graph_color = '#00FF00'
                ),
                right_box_decoration("#000000"),
                separator(),
                left_box_decoration("#336600"),
                icon(" ","#336600"),
                widget.CurrentLayout(
                    background = '#336600',
                    foreground = '#FFFFFF',
                ),
                right_box_decoration("#336600"),
                separator(),
                left_box_decoration("#003300"),
                icon(" ","#003300"),
                 widget.Clock(format="%d/%m/%Y - %H:%M",
                    background = '#003300',
                    foreground = '#FFFFFF'
                ),
                right_box_decoration("#003300"),
            ],
            40,
            background = '#333333'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=13,
    padding=1,
)
extension_defaults = widget_defaults.copy()
