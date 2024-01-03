# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import threading

# local
import module
import window


class CoolDownDataUnit (object):
    def __init__(self):
        self._lock = threading.RLock()
        self.now = 0
        self.max = 0


    def set_value(self, second: int | float):
        """
        ## 设置剩余冷却时间

        second: 剩余冷却 (秒) 若超过最大值则置位
        """
        if not isinstance(second, (int, float)):
            raise TypeError

        if second < 0:
            raise ValueError

        with self._lock:
            value = int(second * 10)

            if value >= self.max:
                self.set()
                return

            self.now = value


    def set_max_value(self, second: int | float, reset: bool = False):
        """
        ## 设置最大冷却时间

        second: 最大冷却时间 (秒)
        reset: 将剩余冷却时间复位
        """
        if not isinstance(second, (int, float)):
            raise TypeError

        if second < 0:
            raise ValueError

        with self._lock:
            self.max = int(second * 10)

        if reset:
            self.clear()


    def set(self, second: int | float = ...):
        """
        ## 置位

        将剩余冷却时间设置为最大值

        second: 若提供该参数则设置最大冷却时间后置位
        """
        with self._lock:
            if isinstance(second, (int, float)):
                self.set_max_value(second)

            self.now = self.max


    def clear(self):
        """
        ## 清除

        将剩余冷却时间置 0
        """
        with self._lock:
            self.now = 0


    def decrease(self) -> bool | None:
        """
        ## 自减

        减少一个刻度的剩余冷却时间
        不会低于 0

        若 剩余时间 已经为 0 返回 True
        若 剩余时间 已经小于 0 返回 False (特殊情况)
        其他情况下返回 None
        """
        with self._lock:
            if self.now == 0:
                return True

            if self.now < 0:
                return False

            self.now -= 1
            return None


    def increase(self) -> bool | None:
        """
        ## 自曾

        增加一个刻度的剩余冷却时间
        不会超过最大值

        若 剩余时间 已经为 最大值 返回 True
        若 剩余时间 已经超过 最大值 返回 False (特殊情况)
        其他情况下返回 None
        """
        with self._lock:
            if self.now == self.max:
                return True

            if self.now > self.max:
                return False

            self.now += 1
            return None


    def is_ready(self) -> bool:
        """
        ## 是否就绪

        若 剩余冷却时间 为 0 返回 True
        其他情况返回 False
        """
        with self._lock:
            result = True if self.now == 0 else False
            return result



class CoolDown (object):
    def __init__(self):
        self.clock_signal = threading.Event()

        self.cd2u_skills: dict[int: CoolDownDataUnit] = {index: CoolDownDataUnit() for index in range(1, 5)}
        self.cd2u_burst: dict[int: CoolDownDataUnit] = {index: CoolDownDataUnit() for index in range(1, 5)}

        self.cd2u_skills_lst: list[CoolDownDataUnit] = [self.cd2u_skills[x] for x in self.cd2u_skills]
        self.cd2u_burst_lst: list[CoolDownDataUnit] = [self.cd2u_burst[x] for x in self.cd2u_burst]

        self.task = threading.Thread(None, self.mainloop, "Cooldown", (), daemon=True)


    # ================================ skills ================================


    def set_skills_cd(self, second: int | float, serial: int = ...):
        """
        ## 设置 元素战技 剩余冷却时间

        second: 剩余冷却 (秒) 若超过最大值则置位
        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        self.cd2u_skills[serial].set_value(second)


    def set_skills_max_cd(self, second: int | float, serial: int = ...):
        """
        ## 设置 元素战技 最大冷却时间

        并将剩余冷却时间复位

        second: 最大冷却时间 (秒)
        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        self.cd2u_skills[serial].set_max_value(second, True)


    def skills_set(self, serial: int = ..., second: int | float = ...):
        """
        ## 元素战技 置位

        将剩余冷却时间设置为最大值

        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        second: 若提供该参数则设置最大冷却时间后置位
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        self.cd2u_skills[serial].set(second)


    def skills_is_ready(self, serial: int = ...) -> bool:
        """
        ## 元素战技 是否就绪

        若 剩余冷却时间 为 0 返回 True
        其他情况返回 False

        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        return self.cd2u_skills[serial].is_ready()


    # ================================ burst ================================


    def set_burst_cd(self, second: int | float, serial: int = ...):
        """
        ## 设置 元素爆发 剩余冷却时间

        second: 剩余冷却 (秒) 若超过最大值则置位
        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        self.cd2u_burst[serial].set_value(second)


    def set_burst_max_cd(self, second: int | float, serial: int = ...):
        """
        ## 设置 元素爆发 最大冷却时间

        并将剩余冷却时间复位

        second: 最大冷却时间 (秒)
        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        self.cd2u_burst[serial].set_max_value(second, True)


    def burst_set(self, serial: int = ..., second: int | float = ...):
        """
        ## 元素爆发 置位

        将剩余冷却时间设置为最大值

        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        second: 若提供该参数则设置最大冷却时间后置位
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        self.cd2u_burst[serial].set(second)


    def burst_is_ready(self, serial: int = ...) -> bool:
        """
        ## 元素爆发 是否就绪

        若 剩余冷却时间 为 0 返回 True
        其他情况返回 False

        serial: 指定角色序号 若为空则自动获取当前前台角色的序号
        """
        if serial is Ellipsis: serial = module.roleserial.get()
        return self.cd2u_burst[serial].is_ready()


    # ================================ base ================================


    def reset(self):
        """
        ## 复位

        重置所有冷却时间
        """
        [unit.clear() for unit in self.cd2u_skills_lst]
        [unit.clear() for unit in self.cd2u_burst_lst]


    def _looptask(self):
        [unit.decrease() for unit in self.cd2u_skills_lst]
        # [unit.decrease() for unit in self.cd2uburst]
        window.cooldown.canvas_update()


    def mainloop(self):
        while True:
            self.clock_signal.wait()
            self.clock_signal.clear()
            try: self._looptask()
            except Exception as _: ...


    def start(self):
        self.task.start()
