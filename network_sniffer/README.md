#  Network Packet Sniffer (ag_sniffer)

A simple Python-based TCP packet sniffer that captures and logs real-time web traffic using [Scapy](https://scapy.net/), and visualizes packet size distribution with [Pandas](https://pandas.pydata.org/) and [Matplotlib](https://matplotlib.org/).

---

## Features

- Captures **TCP packets** on port 80 (HTTP)
- Logs source IP, destination IP, ports, timestamp, and packet size
- Displays a **live terminal TCP packet counter**
- Saves data to `trafik_log.csv`
- Generates a histogram showing packet size distribution

---

##  Example Terminal Output

```
Sniffer başlatıldı.
TCP paketleri yakalanıyor... (Toplam: 42)
```

---

##  Output

- `trafik_log.csv`: Logged packet data
- Histogram: Visual graph of packet size distribution
- Live terminal output showing active packet count

---

##  Requirements

- Python 3.x
- scapy
- pandas
- matplotlib

### Install dependencies:
```bash
pip install scapy pandas matplotlib
```

---

## ▶️ Usage

Run the script with root privileges:
```bash
sudo python3 network_sniffer.py
```

---

##  Roadmap / To Do

- [ ] Add support for UDP and ICMP
- [ ] Port filtering with command-line options
- [ ] Export logs in JSON format
- [ ] Live updating traffic visualization
- [ ] Optional GUI interface (Tkinter or Web-based)

---

##  Author

Selin Sezer – [GitHub](https://github.com/slnszr)  
Project: `network_sniffer`
