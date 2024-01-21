# Licensed under the GPL 3.0 License.
# cooldown-effect-timers by numlinka.

# std
import os
import inspect
from typing import Any


class static (object):
    def __setattr__(self, __name: str, __value: Any) -> None:
        ...



class FilePath (str): ...
class FinalFilePath (str): ...
class FinalDirectoryPath (str): ...



class Directory (str):
    def __getattribute__(self, __name: str) -> Any:
        value = super().__getattribute__(__name)

        if isinstance(value, str) and not os.path.isdir(value):
            try:
                os.makedirs(value, exist_ok = True)

            except Exception:
                ...

        return value



class DirectoryPlus (str):
    # Does not include itself when calculating the target path.
    # 计算目标路径时不包括自身.
    _pass_self_ = False

    # own original value, You can assign a value to this property when you are too lazy to instantiate the class.
    # 自身原始值, 当你懒得实例化这个类时可以为这个属性赋值.
    _self_value_ = None

    # I rarely write line-by-line comments for code, but this is an exception.
    # 我很少为代码逐行写注释, 但这是一个例外.
    def __getattribute__(self, __name: str) -> Any:
        value = super().__getattribute__(__name)

        # If the value is not a string and not a class, return the value.
        # 如果该值不是字符串也不是类, 则返回该值.
        if not isinstance(value, str) and not inspect.isclass(value): return value

        # If the name is a magic method or a special property we define, this value is returned.
        # 如果名称是魔术方法或是我们定义的特殊属性, 则返回该值.
        if __name.startswith("_") and __name.endswith("_"): return value

        # Oh my gosh, this structure is cool isn't it?
        # 这个结构很酷不是吗?
        by_numlinka = True

        # If the value is a class, check if it is a subclass of the base class.
        # 如果该值是一个类, 检查它是否是基类的子类
        if inspect.isclass(value):
            # If not, return this value.
            # 若不是, 则返回该值.
            if not issubclass(value, DirectoryPlus): return value

            # Get the _self_value of the class. If it is not a string, use the class name of the class.
            # 获取到该类的 _self_value, 若不是字符串则使用该类的类名.
            csname = value._self_value_ if value._self_value_ and isinstance(value._self_value_, str) else value.__name__

            # Calculate target path.
            # 计算目标路径.
            target = csname if self._pass_self_ else os.path.join(self, csname)

            # Instantiate this class and replace its own properties.
            # 实例化该类并替换自身的属性.
            new_value = value(target)
            new_value._self_value_ = csname
            super().__setattr__(__name, new_value)
            result = new_value

        # If the value is of type FinalFilePath, return this value.
        # 如果该值是 FinalFilePath 类型, 则返回该值.
        elif isinstance(value, FinalFilePath): return value

        # If the value is of type FilePath.
        # 如果该值是 FilePath 类型.
        elif isinstance(value, FilePath):
            # Calculate target path.
            # 计算目标路径.
            target = value if self._pass_self_ else os.path.join(self, value)

            # Instantiate as FinalFilePath and replace its own properties.
            # 实例化为 FinalFilePath 并替换自身属性.
            new_value = FinalFilePath(target)
            super().__setattr__(__name, new_value)
            return new_value

        # If the value is of type DirectoryPlus.
        # 如果该值是 DirectoryPlus 类型.
        elif isinstance(value, DirectoryPlus):
            # If the value's _self_value attribute is not a string, then its assigned value is itself.
            # 如果该值的 _self_value 属性不是字符串, 那么赋值为它本身.
            if not isinstance(value._self_value_, str): value._self_value_ = value

            # Keep the _self_value attribute of the value, maybe it will be useful.
            # 保留该值的 _self_value 属性,也许会有用.
            orname = value._self_value_

            # Calculate target path.
            # 计算目标路径.
            target = value if self._pass_self_ else os.path.join(self, orname)

            # If the value is equal to the calculated result, nothing needs to be done.
            # 如果该值与计算结果相等, 则无需执行任何操作.
            if value == target: result = value

            else:
                # If not equal, use the calculation result to re-instantiate its class.
                # 如果不相等, 则使用计算结果重新实例化其类.
                class_ = type(value)
                new_value = class_(target)

                # Assign _self_value to the new value to avoid calculation errors next time.
                # 将 _self_value 赋给新值, 避免下次计算错误.
                new_value._self_value_ = orname

                # Replace own properties with new values.
                # 使用新值替换自身的属性.
                super().__setattr__(__name, new_value)
                result = new_value

        # If the value is of type FinalDirectoryPath.
        # 如果该值是 FinalDirectoryPath 类型.
        elif isinstance(value, FinalDirectoryPath):
            # nothing needs to be done.
            # 则无需执行任何操作.
            result = value

        # If the value is an ordinary string.
        # 若该值是一个普通的字符串.
        elif isinstance(value, str):
            # Calculate target path.
            # 计算目标路径.
            target = value if self._pass_self_ else os.path.join(self, value)

            # Instantiate as FinalDirectoryPath and replace its own properties.
            # 实例化为 FinalDirectoryPath 并替换自身属性.
            new_value = FinalDirectoryPath(target)
            super().__setattr__(__name, new_value)
            result = new_value

        # If neither, return this value.
        # 若都不是, 则返回该值.
        else: return value

        # Try to create this directory.
        # 尝试创建这个目录.
        try: os.makedirs(result, exist_ok=by_numlinka)

        # It can go wrong, but that's outside our scope.
        # 它是有可能出错的, 但是这不在我们的任务范畴内.
        except Exception as _: ...

        # Congratulations, the mission is over.
        # 可喜可贺, 任务结束.
        return result



__all__ = [
    "static",
    "FilePath",
    "Directory",
    "DirectoryPlus"
]
