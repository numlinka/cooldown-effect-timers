# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import json
import threading

from typing import Any, Iterable



class Variable (object): ...



class Configuration (object):
    def __init__(self):
        self.__lock = threading.RLock()
        self.__table = {}


    def _get(self, key: str) -> Variable:
        """
        ## Get configuration value
        ## 获取配置值

        ```TEXT
        args:
            key: Configuration name, must be an existing name.
                 配置名称, 必须是现有名称.

        return:
            Variable()
            Returns a special Variable type that works the same as the base type and provides some additional methods.
            返回一个特殊的变量类型, 其工作方式与基本类型相同, 并提供一些额外方法.
        ```
        """
        with self.__lock:
            data = self.__table.get(key, None)

            if data is None:
                raise ValueError("The key does not exist.")

            type_ = data["type"]
            value = data["value"]

            class_ = _VARIABLE_CLASS_TABLE[type_]
            result = class_(value)
            result._set_attribute(self, key)
            return result


    def _get_values(self, key: str) -> tuple[int | float | str] | None:
        """
        ## Get configuration value ranges
        ## 获取配置值范围

        ```TEXT
        args:
            key: Configuration name, must be an existing name.
                 配置名称, 必须是现有名称.

        return:
            list[int | float | str] | None
            Return value range, if not set, return None.
            返回值范围, 若未设置则返回 None.
        ```
        """
        with self.__lock:
            data = self.__table.get(key, None)

            if data is None:
                raise ValueError("The key does not exist.")

            ranges = data["ranges"]

            if ranges is None:
                return None

            else:
                return tuple(ranges)


    def _set(self, key: str, value: int | float | str) -> None:
        """
        ## Set configuration values
        ## 设置配置值

        ```TEXT
        args:
            key: Configuration name, must be an existing name.
                 配置名称, 必须是现有名称.

            value: The set value must be the same as the specified type and cannot be outside the range (if any).
                   设定值, 必须与指定类型相同, 且不能超出范围 (如果有).
        ```
        """
        with self.__lock:
            rule = self.__table.get(key, None)

            if rule is None:
                raise ValueError("The key does not exist.")

            type_ = rule["type"]
            ranges = rule["ranges"]

            if not isinstance(value, type_):
                raise TypeError("The value type is inconsistent with the constraint type.")

            if ranges is not None and value not in ranges:
                raise ValueError("Default values are not in ranges.")

            rule["value"] = value


    def _new(self, key: str, type_: int | float | str, default: int | float | str, ranges: Iterable | None = None) -> None:
        """
        ## Create new configuration
        ## 创建新配置

        ```TEXT
        args:
            key: Configuration name, cannot be repeated.
                 配置名称, 不能重复.

            type_: Data type, only basic data types are supported.
                   数据类型, 仅支持基础数据类型.

            default: Default value, the type must be consistent with the set type.
                     默认值,类型必须与设置的类型一致.

            ranges: The value range cannot exceed this range after setting. The default is None.
                    设置后取值范围不能超出此范围, 默认值为 None.
        ```
        """
        if not isinstance(key, str):
            raise TypeError("The key must be a string.")

        if type_ not in _VARIABLE_CLASS_TABLE:
            raise TypeError("The type_ must be a class.")

        if not isinstance(default, type_):
            raise TypeError("The default value type is inconsistent with the constraint type.")

        if ranges is not None and not isinstance(ranges, Iterable):
            raise TypeError("The ranges must be an iterable object.")

        if ranges is not None and default not in ranges:
            raise ValueError("Default values are not in ranges.")

        with self.__lock:
            if key in self.__table:
                raise ValueError("The key already exists.")

            self.__table[key] = {
                "type": type_,
                "ranges": ranges,
                "default": default,
                "value": default
            }


    def __getattr__(self, __name: str) -> Any:
        return self._get(__name)


    def _load_json(self, filepath: str) -> list[str]:
        """
        ## Load configuration from json file
        ## 从 json 文件加载配置

        ```TEXT
        args:
            filepath: 文件路径

        return:
            list[str]
            Setting failed configuration name.
            设置失败的配置名称.
        ```
        """
        with open(filepath, "r", encoding="utf-8") as fobj:
            content = fobj.read()
            data = json.loads(content)

            if not isinstance(data, dict):
                raise TypeError("The configuration file root type is not dict.")

            lst = []

            for key, value in data.items():
                try:
                    self._set(key, value)

                except Exception as _:
                    lst.append(key)

        return lst


    def _save_json(self, filepath: str) -> None:
        """
        ## Save configuration is json file
        ## 保存配置为json文件

        ```TEST
        args:
            filepath: 文件路径
        ```
        """
        with self.__lock:
            data = {key: self.__table[key]["value"] for key in self.__table}
            content = json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4)

        with open(filepath, "w", encoding="utf-8") as fobj:
            fobj.write(content)



class Variable (object):
    def _set_attribute(self, master: Configuration, target: str) -> None:
        self.__master: Configuration = master
        self.__target: str = target


    def set(self, value) -> Variable:
        """
        ## Set configuration values
        ## 设置配置值

        The value of the object at that time will not be updated after setting. You should get it again from the Configuration object.

        设置后, 此时对象的值不会更新. 您应该从 Configuration 对象中再次获取它.

        ```TEXT
        args:
            value: The set value must be the same as the specified type and cannot be outside the range (if any).
                   设定值, 必须与指定类型相同, 且不能超出范围 (如果有).

        return:
            Variable()
            Returns the updated Variable object.
            返回更新后的 Variable 对象.
        ```
        """
        self.__master._set(self.__target, value)


    def values(self) -> tuple[int | float | str] | None:
        """
        ## Get configuration value ranges
        ## 获取配置值范围

        ```TEXT
        return:
            list[int | float | str] | None
            Return value range, if not set, return None.
            返回值范围, 若未设置则返回 None.
        ```
        """
        return self.__master._get_values(self.__target)

    ranges = values



class IntVariable (int, Variable): ...

class FloatVariable (float, Variable): ...

class StrVariable (str, Variable): ...



_VARIABLE_CLASS_TABLE = {
    int: IntVariable,
    float: FloatVariable,
    str: StrVariable
}

__all__ = [
    "Configuration",
    "Variable",
    "IntVariable",
    "FloatVariable",
    "StrVariable"
]
