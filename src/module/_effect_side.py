# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import threading

# local
import window



class EffectUnit (object):
    def __init__(self, name: str, value: int = 0):
        self._lock = threading.RLock()
        self.name = ""
        self.now = 0
        self.max = 0

        self.set_name(name)
        self.set_max_value(value)


    def set_name(self, name: str):
        """
        ## 设置 effect 名称
        """
        with self._lock:
            self.name = name if isinstance(name, str) else f"{name}"


    def set_value(self, second: int | float):
        """
        ## 设置 effect 时间

        second: 设置 effect 的剩余时间 (秒) 若超过最大值则置位
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


    def set_max_value(self, second: int | float, set_: bool = True):
        """
        ## 设置 effect 的最大时间

        second: 设置 effect 的最大时间 (秒)
        set_: 将效果剩余时间置位
        """
        if not isinstance(second, (int, float)):
            raise TypeError

        if second < 0:
            raise ValueError

        with self._lock:
            self.max = int(second * 10)

        if set_:
            self.set()


    def set(self):
        """
        ## 置位

        将 effect 剩余时间设置为最大时间
        """
        with self._lock:
            self.now = self.max


    def clear(self):
        """
        ## 清除

        将 effect 剩余时间清 0
        """
        with self._lock:
            self.now = 0


    def decrease(self) -> bool | None:
        """
        ## 自减

        减少一个刻度的 effect 剩余时间
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

        增加一个刻度的 effect 剩余时间
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


    def is_close(self) -> bool:
        """
        ## 是否关闭

        若 effect 剩余时间 为 0 返回 True
        其他情况返回 False
        """
        with self._lock:
            result = True if self.now == 0 else False
            return result



class EffectSide (object):
    def __init__(self):
        self._lock = threading.RLock()
        self.clock_signal = threading.Event()

        self._count = 0
        self._count_lock = threading.RLock()

        self._effects: dict[int: EffectUnit] = {}
        self._effect_name_lst: list[str] = []
        self._effect_name_iid: list[int] = []
        self.task = threading.Thread(None, self.mainloop, "Cooldown", (), daemon=True)


    def _update_count(self) -> int:
        with self._count_lock:
            result = self._count
            self._count += 1

        return result


    def _update_cache_list(self):
        with self._lock:
            self._effect_name_lst.clear()
            self._effect_name_iid.clear()

            for iid, unit in self._effects.items():
                unit: EffectUnit
                self._effect_name_lst.append(unit.name)
                self._effect_name_iid.append(iid)


    def add_effect(self, name: str, second: float):
        """
        ## 添加效果

        name: 效果名称
        value: 效果持续时间 (秒)
        """
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(second, (int, float)):
            raise TypeError

        iid = self._update_count()

        unit = EffectUnit(name, second)

        with self._lock:
            self._effects[iid] = unit
            self._update_cache_list()


    def set_effect(self, name: str, second: float = ..., much: int = ..., reverse: bool = False):
        """
        ## 设置效果

        如果效果名称已存在则重置持续时间，
        不存在则添加该效果

        name: 效果名称
        value: 效果持续时间 (秒) 若效果名称已存在且未设置该值时则沿用之前的设置
        much: 要重置的数量 默认重置所有效果
        reverse: 反向查找 从列表末尾开始查找
        """
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(second, (int, float)) and second is not Ellipsis:
            raise TypeError

        if not isinstance(much, int) and much is not Ellipsis:
            raise TypeError

        if much is not Ellipsis and much <= 0:
            return

        with self._lock:
            if not self.exist(name):
                self.add_effect(name, second)
                return

            _name_lst = self._effect_name_lst[::-1] if reverse else self._effect_name_lst.copy()
            _name_iid = self._effect_name_iid[::-1] if reverse else self._effect_name_iid.copy()

            indices = [index for index, exname in enumerate(_name_lst) if name == exname]
            indexes = indices if much is Ellipsis else indices[:much]
            iid_lst = [_name_iid[index] for index in indexes]

            for iid in iid_lst:
                unit = self._effects[iid]
                unit: EffectUnit

                if second is Ellipsis:
                    unit.set()
                    continue

                unit.set_max_value(second)


    def del_effect(self, name: str, much: int = ..., reverse: bool = False):
        """
        ## 移除效果

        name: 效果名称
        much: 要移除的数量 默认移除所有效果
        reverse: 反向查找 从列表末尾开始查找
        """
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(much, int) and much is not Ellipsis:
            raise TypeError

        if much is not Ellipsis and much <= 0:
            return

        with self._lock:
            if not self.exist(name):
                return

            _name_lst = self._effect_name_lst[::-1] if reverse else self._effect_name_lst
            _name_iid = self._effect_name_iid[::-1] if reverse else self._effect_name_iid

            indices = [index for index, exname in enumerate(_name_lst) if name == exname]
            indexes = indices if much is Ellipsis else indices[:much]
            iid_lst = [_name_iid[index] for index in indexes]

            for iid in iid_lst:
                del self._effects[iid]

            self._update_cache_list()


    def exist(self, name: str) -> bool:
        """
        ## 效果是否存在
        """
        if not isinstance(name, str):
            raise TypeError

        with self._lock:
            result = name in self._effect_name_lst

        return result


    def exist_much(self, name: str) -> int:
        """
        ## 效果存在数量
        """
        if not isinstance(name, str):
            raise TypeError

        with self._lock:
            lst = [exname for exname in self._effect_name_lst if name == exname]

        return len(lst)


    def clear_all_effect(self):
        """
        ## 清除所有效果
        """
        with self._lock:
            for iid, unit in self._effects.items():
                unit: EffectUnit
                unit.clear()


    def get(self) -> list[EffectUnit]:
        with self._lock:
            result = [self._effects[x] for x in self._effects]
            return result


    def _looptask(self):
        with self._lock:
            lst = [x for x in self._effects]

            for iid in lst:
                result = self._effects[iid].decrease()
                if result: del self._effects[iid]

            self._update_cache_list()

        window.effectside.canvas_update()


    def mainloop(self):
        while True:
            self.clock_signal.wait()
            self.clock_signal.clear()
            try: self._looptask()
            except Exception as _: ...


    def start(self):
        self.task.start()
