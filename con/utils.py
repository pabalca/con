import dbus


class Systemd():
    def __init__(self):
        bus = dbus.SystemBus()
        systemd = bus.get_object(
            'org.freedesktop.systemd1',
            '/org/freedesktop/systemd1'
        )

        self.manager = dbus.Interface(
            systemd,
            'org.freedesktop.systemd1.Manager'
        )

    def status(self, unit_name):
        all_units = self.list_units()
        for unit in all_units:
            service = unit[0].split("/")[-1]
            if service == unit_name:
                loaded = unit[1]
                status = unit[2]
                active = unit[3]
                return active, status
        return None

    def list_units(self):
        units = self.manager.ListUnits()
        return units


    def start(self, service):
        result = self.manager.StartUnit(service, 'fail')
        return result

    def stop(self, service):
        result = self.manager.StopUnit(service, 'fail')
        return result

