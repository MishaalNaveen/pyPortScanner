# 🔍 pyPortScanner — Custom TCP Port Scanner in Python

**pyPortScanner** is a lightweight, multithreaded TCP port scanner written in Python.  
It performs real-time port scanning, grabs service banners, maps ports to known services, and saves detailed scan reports to file.

This project was built from scratch to understand how tools like Nmap work *under the hood* — using only low-level Python sockets and threading.

---

## ⚙️ Features

- 🌐 Domain to IP resolution
- 🔁 Multithreaded TCP scanning
- 📡 Banner grabbing from open ports
- 🧠 Common service name detection (e.g., SSH, HTTP, FTP)
- 📝 Saves scan results to `.txt` file
- ⏱ Scan duration timer
- ❌ Optional flag to show closed ports
- 📁 Modular structure (`services.py`)

---

## 💻 Demo Output

```bash
$ python3 scanner.py scanme.nmap.org -p 20-100

🌐 Target: scanme.nmap.org (45.33.32.156)

🔍 Scanning ports 20 to 100...

🔓 Open: Port 22 (SSH) — Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
🔓 Open: Port 80 (HTTP) — Banner: Apache/2.4.7 (Ubuntu) + HTML Response

✅ Scan results saved to: results_scanme_nmap_org.txt

⏱ Completed in 1.34 seconds.
```

---

## 📦 Usage

```bash
python3 scanner.py <target> -p <start-end> [--show-closed]
```

**Examples:**

```bash
python3 scanner.py scanme.nmap.org -p 1-1024
python3 scanner.py 192.168.1.1 -p 20-80 --show-closed
```

---

## 🧠 Why I Built This

I’ve been learning about active reconnaissance and Nmap. To understand scanning at a deeper level, I built this tool using Python sockets and threading — and tested it ethically on [scanme.nmap.org](https://nmap.org).

---

## 📁 Project Structure

```
pyPortScanner/
├── scanner.py       # Main scanner script
├── services.py      # Port-to-service dictionary (modular)
├── README.md        # This file
├── results_*.txt    # Output files (auto-generated)
```

---

## 🛡️ Disclaimer

This tool is built **for learning purposes only.**  
Please scan only hosts you **own** or have **explicit permission** to scan (like `scanme.nmap.org`). Unauthorized scanning is illegal.

---

## ✍️ Author

Built with curiosity and zero budget by a cybersecurity student 💻🔐  
If you find it helpful, feel free to ⭐ the repo!
