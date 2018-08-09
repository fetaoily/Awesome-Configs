#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


def check_tcp_port(kw, timeout=3):
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (str(kw["host"]), int(kw["port"]))
    cs.settimeout(timeout)
    try:
        status = cs.connect_ex(address)
    except Exception:
        result_msg = {"status": False, "message": str(e), "info": "tcp check"}
    else:
        if status != 0:
            result_msg = {
                "status": False,
                "message": "Connection %s:%s failed" % (kw["host"], kw["port"]),
                "info": "tcp check"
            }
        else:
            result_msg = {"status": True, "message": "OK", "info": "tcp check"}
    return result_msg


for i in range(0, 100000000):
    result_msg = check_tcp_port({"host": "123.125.210.228", "port": "80"})
    print(str(i), str(result_msg))
    pass
