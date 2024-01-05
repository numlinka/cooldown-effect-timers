# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import tkinter

# site
import ttkbootstrap


class motion_window_by_canvas (object):
    def __init__(self, window: ttkbootstrap.Window, widget: ttkbootstrap.Canvas, tag: str, extra: object = ...):
        self.window = window
        self.widget = widget
        self.tag = tag
        self.extra = extra
        self.widget.tag_bind(tag, "<Button-1>", self.start_drag)
        self.widget.tag_bind(tag, "<B1-Motion>", self.on_drag)
        self.start_x = 0
        self.start_y = 0


    def start_drag(self, event: ttkbootstrap):
        self.start_x = event.x
        self.start_y = event.y


    def on_drag(self, event):
        x = self.window.winfo_x() - self.start_x + event.x
        y = self.window.winfo_y() - self.start_y + event.y
        self.window.geometry(f"+{x}+{y}")
        if callable(self.extra): self.extra(self, event)


def center_window(window: ttkbootstrap.Window, window_width: int = ..., window_height: int = ..., set_window_size: bool = False):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    width = window.winfo_width() if window_width is Ellipsis else window_width
    height = window.winfo_height() if window_height is Ellipsis else window_height

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    result = f"{width}x{height}+{x}+{y}" if set_window_size else f"+{x}+{y}"

    window.geometry(result)


def set_window_icon(window: ttkbootstrap.Window, icon_path: str):
    try:
        window.iconbitmap(default=icon_path)
        window.iconbitmap(bitmap=icon_path)

    except Exception as e:
        ...


class combobox_do_not_want_selection (object):
    def __init__(self, combobox: ttkbootstrap.Combobox):
        self.combobox = combobox
        self.combobox.bind("<<ComboboxSelected>>", self.selection_clear, True)
        self.combobox.bind("<FocusIn>", self.selection_clear, True)
        self.combobox.bind("<FocusOut>", self.selection_clear, True)

    def selection_clear(self, *_):
        self.combobox.selection_clear()
