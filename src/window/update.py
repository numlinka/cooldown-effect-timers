# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import webbrowser

# site
import requests

from ttkbootstrap.dialogs.dialogs import Messagebox
from ttkbootstrap.localization import msgcat

# local
import env


def check(*_):
    try:
        handle = requests.get("https://cooldown-effect-timers.numlinka.com/index.json")
        content = handle.json()
        version_code = content["version_code"]
        site = content["site"]
        if version_code <= env.version_code:
            return

        # 我承认 ttkbootstrap 做了本地化工作这个事情很好
        # 但是这个设计用在 Messagebox 的返回值上会显得很费解
        # 明明返回布尔值就行的事情非要返回一个本地化字符串
        # 这导致想要准确判断用户的交互会变得麻烦
        result = Messagebox.okcancel(title="更新检查", message=f"{env.PROJECT} 有更新可用\n是否前往下载更新?")
        if result == msgcat.MessageCatalog.translate("OK"):
            webbrowser.open(site)


    except Exception as _:
        ...
