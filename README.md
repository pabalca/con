# con[trol] the system.

```
 $ con
Usage: con [OPTIONS] COMMAND [ARGS]...

  con[trol] the system (v1) @ pabalca

Options:
  --help  Show this message and exit.

Commands:
  status
  start
  stop
```

#### Install system dependencies
```
sudo apt-get install python-dbus
```

#### Virtualenv
```
python3 -m venv --system-site-packages my_venv
```

#### Systemd dbus api
https://www.freedesktop.org/software/systemd/man/systemd.service.html

