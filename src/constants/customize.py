# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

README = """cooldown-effect-timers - customize / 自定义

在大部分情况下我不会主动去实现新的角色事件

如果你发现某个角色事件没有实现
或者你发现某个角色事件实现的不够好
那么你可以尝试以下几种方法方式


1. 向我提交需求

你可以通过

- 邮箱 ( numlinka@163.com )
- issues ( https://github.com/numlinka/cooldown-effect-timers/issues )
- 爱发电 ( https://afdian.net/a/numlinka )
- QQ 群 ( 目前没有 )

或其他方式联系我并提供相关需求



2. 通过自定义的方式添加新的角色事件

我会提供一些具有良好可行性的方式供你尝试添加新的角色事件
例如

- lua 脚本

如果有需要，我会提供更多更简便的方式
当然如果你有计算机基础，也可以向我递交你的设计方案



3. 向我提交代码

这是最简单的的方案 ( 对于我来说 )
你可以直接向我提交代码
可以选择提交一个 pull request
或者向我发送一封邮件



4. 嚎啕大哭

如果你真的没有其他办法了


"""


LUAROLE = """cooldown-effect-timers - customize.lua

我提供了一个 lua 解释器
你可以通过它来实现新的角色事件


使用 lua 脚本实现的角色事件的步骤如下

在 .sldata\customize\lua 目录下创建一个文件
文件名为角色事件的名称
文件后缀名为 .lua
例如角色事件名为 "胡桃"
则文件名为 "胡桃.lua"

文件内容如下

你可以选择性的提供以下属性 ( 变量 )

role_name = "胡桃", -- 角色名称 ( 不写也行，默认为文件名 )
cd_skills = 16, -- 元素技能冷却时间 ( 秒 )
cd_burst = 15, -- 元素爆发 ( 秒 )

选择性的提供以下函数

switch_in() -- 角色进入 ( 切换到该角色 ) 时
switch_out() -- 角色离开 ( 切换到其他角色 ) 时
press_skills() -- 按下 ( 点击 ) 元素技能 ( 按键 ) 时
release_skills() -- 松开 ( 释放 ) 元素技能 ( 按键 ) 时
press_burst() -- 按下 ( 点击 ) 元素爆发 ( 按键 ) 时
release_burst() -- 松开 ( 释放 ) 元素爆发 ( 按键 ) 时

更详细的文档可以参考

https://cooldown-effect-timers.numlinka.com/#/customize/lua



当然，你可以使用其他人提供的 lua 脚本
但要注意，使用前请检查其安全性



"""