# Key points for python import (VERY IMPORTANT)

* The relative import of Python only works when a module file
is not the execution start script(top-level script),
so if your module files contain unit test code
and you want to run it for unit test,
please go to root directory and run
```
$ python -m dir1.dir2.moduleName
```
For example, go to the directory relative-import/ and run
```
$ python -m mypackages.subpackages.module_x
```
Note that `-m` means "it is a module." and we dont need the extension `.py`.

* When you run `python demo_relative_start.py`, top-level is where `demo_relative_start.py` located in.

* When you run `python -m mypackages.subpackages.module_x`, top-level is where you run python command.

* If you go to `relative-import/mypackages`, and run `python -m subpackages.module_x`,
you'll get an error message like "ValueError: attempted relative import beyond top-level package",
that's because `module_x.py` uses relative import path referenced to
where you run python command (`relative-import/mypackages`),
and this would cause this error. ("top-level" means the directory where you run python command)

* No matter you want to run unit tests or project starting scripts,
please always run them in project root. For project starting scripts,
we just run `python xxx.py` and don't need `-m`. For example,
go to the directory relative-import/ and run `python demo_relative_start.py`.
