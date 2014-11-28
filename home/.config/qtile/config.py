from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod4"
xsnap = "DATE=`date +%d%m%Y_%H%M%S`; xsnap -nogui -file $HOME/screenshot/xsnap-$DATE.png"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "h",      lazy.to_screen(1)),
    Key([mod], "l",      lazy.to_screen(0)),

    # for open terminal [+sb turn off scrollbar] [-e execute command]
    Key([mod], "Return", lazy.spawn("urxvt +sb -e tmux")),
    # make screenshot
    Key([mod, "control"], "i", lazy.spawn(xsnap)),
    Key([mod], "b", lazy.spawn("chromium")),
    #screensaver setted at 5 min for company rules
    Key([mod, "control"], "l", lazy.spawn("xscreensaver-command -lock")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),

    # for Tile layout
    Key([mod, "shift"], "i", lazy.layout.increase_ratio()),
    Key([mod, "shift"], "d", lazy.layout.decrease_ratio()),
]

groups = [
    Group("a"),
    Group("s"),
    Group("d"),
    Group("f"),
    Group("u"),
    Group("i"),
    Group("o"),
    Group("p"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.Max(),
    layout.Stack(stacks=2)
]

screens = [
    Screen(
        bottom = bar.Bar(
                    [
#                        widget.GroupBox(),
#                        widget.Prompt(),
#                        widget.WindowName(),
#                        widget.Battery(
#                        energy_now_file='charge_now',
#                        energy_full_file='charge_full',
#                        power_now_file='current_now',
#                        update_delay = 5,
#                        foreground = "7070ff",),
#                        widget.TextBox("desktop", name="default"),
#                        widget.Systray(),
#                        widget.Clock('%Y-%m-%d %H:%M'),
                    ],
                    30,
                ),
    ),
    Screen(
        bottom = bar.Bar(
                    [
                        widget.GroupBox(),
                        widget.Prompt(),
                        widget.WindowName(),
                        widget.TextBox("desktop", name="default"),
                        widget.Systray(),
                        widget.Clock('%Y-%m-%d %H:%M'),
                    ],
                    30,
                ),
    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
                start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
                start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#mouse = ()
widget_defaults = {}
dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
wmname = "qtile"
