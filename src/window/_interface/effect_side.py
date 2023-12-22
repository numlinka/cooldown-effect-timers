# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# site
import ttkbootstrap

# local
import window


class EffectSide (object):
    def __init__(self, master: ttkbootstrap.Frame):
        self.master = master

        self.v_moving_block = ttkbootstrap.BooleanVar()

        self.wfe_moving_block = ttkbootstrap.Frame(self.master)
        self.wfe_moving_block.pack(side="top", fill="x", padx=5, pady=5)

        self.wll_moving_block = ttkbootstrap.Label(self.wfe_moving_block, text="显示移动块 (按住可拖动悬浮窗)")
        self.wcb_moving_block = ttkbootstrap.Checkbutton(self.wfe_moving_block, bootstyle="success-square-toggle", variable=self.v_moving_block, command=self.bin_moving_block)
        self.wll_moving_block.pack(side="left")
        self.wcb_moving_block.pack(side="right")


    def bin_moving_block(self, *_):
        window.effectside.moving_blocks(self.v_moving_block.get())
