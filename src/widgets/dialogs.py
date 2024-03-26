# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import copy
import tkinter

# site
import ttkbootstrap
from ttkbootstrap.constants import *

# local
import window


class ChoiceListbox (object):
    def __init__ (
            self,
            title: str = "",
            options: list[str] = ...,
            *,
            window_width: int = 300,
            window_height: int = 240,
            parent: ttkbootstrap.Window = None
            ):

        self.title = title
        self.options = copy.deepcopy(options)
        self.window_width = 300 if not isinstance(window_width, int) or window_width < 100 else window_width
        self.window_height = 240 if not isinstance(window_height, int) or window_height < 100 else window_height
        self.parent = parent

        self.result = ""
        self.refresh_allow = True

        self._initial_window()
        self._initial_widget()
        self.refresh()


    def _initial_window(self):
        self.window = ttkbootstrap.Toplevel()
        self.window.title(self.title)
        self.window.transient(self.parent)
        self.window.grab_set()
        self.window.focus_set()
        window.method.center_window_for_window(self.window, self.parent, self.window_width, self.window_height, True)


    def _initial_widget(self):
        self.v_input = ttkbootstrap.StringVar()

        self.wfe_input = ttkbootstrap.Frame(self.window)
        self.wfe_options = ttkbootstrap.Frame(self.window)
        self.wfe_input.pack(side=TOP, fill=X, padx=5, pady=5)
        self.wfe_options.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=(0, 5))

        self.wet_input = ttkbootstrap.Entry(self.wfe_input, textvariable=self.v_input)
        self.wbt_sure = ttkbootstrap.Button(self.wfe_input, text="确定", command=self.sure)
        self.wlb_list = tkinter.Listbox(self.wfe_options)
        self.wsb_list = ttkbootstrap.Scrollbar(self.wlb_list, orient=VERTICAL, command=self.wlb_list.yview)
        self.wlb_list.configure(yscrollcommand=self.wsb_list.set)

        self.wet_input.pack(side=LEFT, fill=X, expand=True)
        self.wbt_sure.pack(side=RIGHT, padx=(5, 0))
        self.wlb_list.pack(side=LEFT, fill=BOTH, expand=True)
        self.wsb_list.pack(side=RIGHT, fill=Y)

        self.v_input.trace_add("write", self.refresh)
        self.wlb_list.bind("<<ListboxSelect>>", self.choice)
        self.wlb_list.bind("<Double-1>", self.double)


    def refresh(self, *_):
        if not self.refresh_allow: return
        value = self.v_input.get()
        self.wlb_list.delete(0, END)

        lst = self.options if not value else [option for option in self.options if value in option]

        for option in lst:
            self.wlb_list.insert(END, option)


    def choice(self, *_):
        index = self.wlb_list.curselection()
        if not index: return
        value = self.wlb_list.get(index[0])

        self.refresh_allow = False
        self.v_input.set(value)
        self.refresh_allow = True


    def sure(self, *_):
        self.result = self.v_input.get()
        self.close()


    def double(self, *_):
        index = self.wlb_list.curselection()
        if not index: return
        self.sure()


    def close(self, *_):
        self.window.destroy()


    def wait(self):
        self.window.wait_window()
        return self.result



def choicelistbox (
            title: str = "",
            options: list[str] = ...,
            *,
            window_width: int = 300,
            window_height: int = 240,
            parent: ttkbootstrap.Window = None
    ) -> str:
    kwargs = locals()
    kernel = ChoiceListbox(**kwargs)
    result = kernel.wait()
    return result
