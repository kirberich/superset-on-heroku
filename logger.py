from superset.utils.log import AbstractEventLogger
import json


class JSONStdOutEventLogger(AbstractEventLogger):
    def log(self, user_id, action, *args, **kwargs):
        records = kwargs.get("records", list())
        dashboard_id = kwargs.get("dashboard_id")
        slice_id = kwargs.get("slice_id")
        duration_ms = kwargs.get("duration_ms")
        referrer = kwargs.get("referrer")

        for record in records:
            log = dict(
                action=action,
                json=record,
                dashboard_id=dashboard_id,
                slice_id=slice_id,
                duration_ms=duration_ms,
                referrer=referrer,
                user_id=user_id,
            )
            print(json.dumps(log))
