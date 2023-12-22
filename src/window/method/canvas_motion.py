# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap



class motion_window_by_canvas (object):
    def __init__(self, window: ttkbootstrap.Window, widget: ttkbootstrap.Canvas, tag: str):
        self.window = window
        self.widget = widget
        self.tag = tag
        self.widget.tag_bind(tag, "<Button-1>", self.start_drag)


    def start_drag(event):
        # 鼠标按下事件处理函数
        widget = event.widget
        widget.start_x = event.x
        widget.start_y = event.y


    def on_drag(self, event):
        # 鼠标拖动事件处理函数
        widget = event.widget
        x = self.window.winfo_x() - widget.start_x + event.x
        y = self.window.winfo_y() - widget.start_y + event.y
        self.window.geometry(f"+{x}+{y}")
