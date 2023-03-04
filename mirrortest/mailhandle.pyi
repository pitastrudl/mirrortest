import typing

class BaseController(object):
	def __init__(self, name :str) -> None: ...

	def open(self, filename :str) -> bool | int | None: ...


class Controller(BaseController):
	def __init__(self, *args :list[typing.Any]) -> None: ...

	def _invoke(self, cmdline :str) -> int: ...

	def open(self, filename :str) -> bool | int: ...


class Start(BaseController):
	def open(self, filename :str) -> bool: ...

def _isexecutable(cmd :str) -> bool: ...

def _iscommand(cmd :str) -> bool: ...

class KfmClient(Controller):
	def __init__(self, kfmclient :str = 'kfmclient') -> None: ...

	def detect_kde_version(self) -> None | str: ...

	def fixreturncode(self, returncode :int | None) -> int: ...

def detect_desktop_environment() -> str: ...

def register_X_controllers() -> None: ...

def get() -> bool: ...

def open(filename :str) -> bool: ...

def _fix_addersses(**kwargs :typing.Dict[str, str]) -> typing.Dict[str, str]: ...

def mailto_format(**kwargs :typing.Dict[str, str]) -> str: ...

def mailto(address :str, to :str | None = None, cc :str | None = None, bcc :str | None = None, subject :str | None = None, body :str | None = None) -> bool: ...