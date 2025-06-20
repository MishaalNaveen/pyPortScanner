import socket
import argparse
import threading
from datetime import datetime
from services import common_ports
import time

results = [] 

def get_probe_payload(port):
    if port == 80 or port == 8080:
        return b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    else:
        return b"\r\n"

# Scan one port
def check_port(ip, port, show_closed=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            res = s.connect_ex((ip, port))
            if res == 0:
                try:
                    s.send(get_probe_payload(port))
                    banner = s.recv(1024).decode(errors="ignore").strip()
                except:
                    banner = "No banner"
                service = common_ports.get(port, "Unknown")
                result = f"🔓 Open: Port {port} ({service}) — Banner: {banner}"
                print(result)
                results.append(result)
            else:
                if show_closed:
                    print(f"❌ Closed: Port {port}")
    except Exception as e:
        print(f"[!] Error on port {port}: {e}")


def start_scan(ip, start_port, end_port, show_closed=False):
    print(f"\n🔍 Scanning ports {start_port} to {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=check_port, args=(ip, port, show_closed))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def write_report(target, results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"results_{target.replace('.', '_')}.txt"
    with open(filename, 'w') as f:
        f.write(f"Scan Report for {target} — {timestamp}\n")
        f.write("="*60 + "\n")
        for line in results:
            f.write(line + "\n")
    print(f"\n✅ Scan results saved to: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🛡️ pyPortScanner - Custom Python Port Scanner")
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan (e.g. 20-100)")
    parser.add_argument("--show-closed", action="store_true", help="Show closed ports too")
    args = parser.parse_args()

    # Resolve host
    try:
        ip = socket.gethostbyname(args.target)
        print(f"\n🌐 Target: {args.target} ({ip})")
    except socket.gaierror:
        print("[!] Invalid hostname.")
        exit()

    # Parse range
    try:
        start_port, end_port = map(int, args.ports.split("-"))
    except:
        print("[!] Invalid port range. Use format: 20-80")
        exit()

    scan_start = time.time()
    start_scan(ip, start_port, end_port, args.show_closed)
    scan_end = time.time()

    write_report(args.target, results)

    duration = round(scan_end - scan_start, 2)
    print(f"\n⏱️ Completed in {duration} seconds.")
