# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.


TRANSPARENTCOLOR = "grey"

TEXT_ABOUT = """cooldown-effect-timers - About / 关于

cooldown-effect-timers 是一个免费 ( free ) 开源 ( open source ) 软件
对于软件的修改和再分发请遵守 GNU General Public License v3.0 协议


cooldown-effect-timers 并非用于商业用途，仅限个人使用。
该工具仅供学术研究和交流目的，如果您选择使用，请自行承担风险。


cooldown-effect-timers 不会以任何形式收集您的任何信息，
也不会将您的任何信息上传到任何服务器。


对于软件的 bug 反馈或建议，请在 GitHub 页面提交 issue
或发送邮件至 numlinka@163.com


如果你喜欢这个工具可以前往爱发电页面赞助
或帮助宣传，这些都是友好的支持方式


项目贡献者
    - numLinka ( 软件开发者 )
        - 邮箱: numlinka@163.com
        - 爱发电: https://afdian.net/a/numlinka


有关 cooldown-effect-timers 的更多信息请访问
    - https://github.com/numlinka/cooldown-effect-timers


cooldown-effect-timers ( 原神技能冷却时间和效果持续时间计时器 )
由 numLinka 提供技术支持


"""

TEXT_HELP = """cooldown-effect-timers - HELP / 帮助

cooldown-effect-timers 是一个免费 ( free ) 开源 ( open source ) 软件
对于软件的修改和再分发请遵守 GNU General Public License v3.0 协议



0x00. 前言

cooldown-effect-timers 不会监听、读取或修改游戏内存，
所有的数据均由程序自身进行推断和计算。



0x01. 首先

请使用管理员权限运行本软件
否则按键监听可能无法正常工作



0x02. 其次

你需要使用窗口化 ( 或无边框窗口 ) 运行游戏
否则你将无法看到计时器的悬浮窗

在全屏游戏下点击公告，游戏会变成无边框窗口



0x03. 角色

在 Role ( 角色 ) 页面左侧指定对应位置的角色
需要在下拉框中选择或使用鼠标滚轮切换角色

在下拉框中直接输入文字不会被识别



0x04. 武器

在 Role ( 角色 ) 页面右侧指定对应位置的武器
需要在下拉框中选择或使用鼠标滚轮切换武器

在下拉框中直接输入文字不会被识别

*注意：目前还没有实现武器的基础事件类
所以该功能暂时无法使用



0x05. 冷却

在 Cooldown ( 冷却 ) 页面点击显示移动块
会在悬浮窗左上角显示移动块
按住移动块可以拖动悬浮窗

可以通过滑块和输入框或使用鼠标滚轮
调整每个角色冷却条的间距
1080P 推荐为 97 ( 默认值 )
其他分辨率请自行调整

当前焦点 ( 前台 ) 角色会在对应冷却条右侧显示三角箭头



0x06.  效果

在 Effect ( 效果 ) 页面点击显示移动块
会在悬浮窗左上角显示移动块
按住移动块可以拖动悬浮窗

点击显示基线可以在悬浮窗上显示基线
基线表示了延生的起始位置
不同的显示模式下基线的位置也会有差异

可以通过下拉框调整显示模式
选择一个你喜欢的就好

可以通过滑块和输入框或使用鼠标滚轮
调整效果最大效果显示数量 ( 默认为 8 )
不推荐调整这个值
太小的值会导致效果显示不全
太大的值会带来性能问题



0x07. 按键

键盘主键区 1 2 3 4 切换焦点角色
对应游戏中的角色切换

键盘主键区 Q E 发送技能消息
对应游戏中的技能按键

键盘数字区 . (del) 清除所有冷却和效果

防水溅不防手贱



0x08. 更新

该项目没有配备自动更新组件
请自行下载最新版本并覆盖原文件
或者前往 GitHub 页面下载最新版本
并将其覆盖原文件



0x09. 扩展

cooldown-effect-timers 会在后续的版本中提供更多功能
例如可以支持更多角色事件
或提供配置文件让用户自己编写角色事件
效果上可能会比内置的差一些



0x10. 缺失

内置的角色事件通常是我个人常用的角色
我会测试它在游戏中的使用效果
并尽量保证内置的角色事件的正确性
但我并不能保证所有角色的效果都能被正确计算
所以如果您有更好的角色事件，欢迎提交 issue

由于我并不是全角色的玩家
所以有些我没有的角色可能会因为无法测试而不会被内置

如果你喜欢的角色事件没有被内置
可以尝试联系开发者 ( 我 ) 更进
当然，也有可能是我没有那个角色



0x11. 提议

如果您有更好的建议或想法
请在 GitHub 页面提交 issue
或发送邮件至 numlinka@163.com
或通过其他方式联系我



0x12. 赞助

如果你喜欢这个工具可以前往爱发电页面赞助
或在 GitHub 给我一个 star 吧

爱发电
    - https://afdian.net/a/numlinka

GitHub
    - https://github.com/numlinka/cooldown-effect-timers


其他详情信息请查看关于页面


"""


__all__ = [
    "TRANSPARENTCOLOR",
    "TEXT_ABOUT"
]
