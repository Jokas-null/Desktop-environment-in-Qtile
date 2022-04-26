from libqtile import layout
from libqtile.config import Match

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # layout.Stack(num_stacks=2),//
    # layout.Bsp(),//
    # layout.Matrix(),//
    # layout.MonadTall(),//
    #layout.MonadWide(),
    #layout.RatioTile(),not bad
    #layout.Tile(), not bad
    #layout.TreeTab(),definitivamente no
    layout.VerticalTile(),
    #layout.Zoomy(),definitivamente no
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  
        Match(wm_class="makebranch"),  
        Match(wm_class="maketag"), 
        Match(wm_class="ssh-askpass"),  
        Match(title="branchdialog"),  
        Match(title="pinentry"),  
    ]
)