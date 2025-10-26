import socket
import psutil

def run():
    data = {}
    data["hostname"] = socket.gethostname()
    data["ip_address"] = socket.gethostbyname(socket.gethostname())
    data["open_ports"] = [conn.laddr.port for conn in psutil.net_connections() if conn.status == 'LISTEN']
    return data
