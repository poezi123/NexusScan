import socket
from colorama import Fore
from scapy.all import sniff, IP, TCP, UDP, ICMP
import threading
import time
import os
# Bildschirm löschen
os.system('cls' if os.name == 'nt' else 'clear')

# Farbcodes
RED = "\033[31m"
RESET = "\033[0m"
# ASCII Banner
HACKTOOL = r"""
        _      ________  _ _     ____  ____  ____  ____  _     
        / \  /|/  __/\  \/// \ /\/ ___\/ ___\/   _\/  _ \/ \  /|
        | |\ |||  \   \  / | | |||    \|    \|  /  | / \|| |\ ||
        | | \|||  /_  /  \ | \_/|\___ |\___ ||  \__| |-||| | \||
        \_/  \|\____\/__/\\\____/\____/\____/\____/\_/ \|\_/  \|
"""
intro = """
        Creator: S1BERIA                               VERSION: 1.2 FREE
        Date: 08.04.2026                               Penetration Testing
"""
auswahl = """
        ╔═══    SIMPLE TOOLS    ═══╗
         1. Port scanner
        ║2. Packet Sniffer         ║
         3. IP-MAC Mapper (Admin)
        ╚═══                    ═══╝
"""
# Anzeige in Rot
print(RED + HACKTOOL + RESET)
print(RED + intro + RESET)
print(auswahl)
auswahl1 = input(f"""{Fore.RED}
┌───({Fore.WHITE}User@nexusscan{Fore.RED})─[{Fore.WHITE}~/1{Fore.RED}]                    
└──$  {Fore.WHITE}""")

match auswahl1:
    case "1":
        port_scanner_ascii = r"""  1
                _.-----._
             .'.-'''''-.'._
            //`.:#:'    `\\\
           ;; '           ;;'.__.===============,
           ||             ||  __ Port Scanner   )
           ;;             ;;.'  '==============='
            \\           ///
              ':.._____..:'~
                `'-----'`
        
        """
        print(port_scanner_ascii)
        
        def scan_port(ip, port):
            sock = socket.socket()
            sock.settimeout(1.5)  # Timeout etwas erhöht für Banner-Antworten
            try: 
                sock.connect((ip, port))
                
                # --- NEU: Banner Grabbing ---
                try:
                    # Wir versuchen, eine Identifikation vom Dienst zu erhalten
                    banner = sock.recv(1024).decode().strip() #sock.recv(1024) liest daten vom socket max 1024 bytes, wartet auf Antwort vom Server / .decode() wandelt bytes in string um / .strip() das entfernt leerzeichen usw
                    if not banner:
                        # Falls keine Antwort kommt, versuchen wir den Standardnamen
                        banner = socket.getservbyport(port, "tcp")
                except:
                    # Falls der Dienst nicht sofort antwortet (z.B. HTTP)
                    try:
                        banner = socket.getservbyport(port, "tcp")
                    except:
                        banner = "Unbekannter Dienst"
                
                print(f"Port {port:5} [OFFEN] -> Dienst: {banner}")
                # ----------------------------

            except:
                pass
            finally:
                sock.close()

        def scan_range(ip, start, end):
            threads = []
            for port in range(start, end + 1):
                t = threading.Thread(target=scan_port, args=(ip, port))
                t.start()
                threads.append(t)
            
            for t in threads:
                t.join()

        # Eingaben
        ip = input("IP-Adresse: ")
        start_port = int(input("Startport: "))        
        end_port = int(input("Endport: "))  

        print(f"\nScanne {ip} von Port {start_port} bis {end_port}...\n")
        scan_range(ip, start_port, end_port)
        print("\nScan fertig!")
            

    case "2":
        packet_box = r"""
       __________
      /         /|
     /_________/ |
    | PACKET  |  |
    | SNIFFER|  |
    |_________| /
    (_________)/ 
"""

        print(packet_box)
        last_packet_time = time.time()
        IDLE_TIMEOUT = 10

        # Dictionary für IP → Farbe
        ip_colors = {}
        colors = [
            "\033[91m",  # rot
            "\033[92m",  # grün
            "\033[93m",  # gelb
            "\033[94m",  # blau
            "\033[95m",  # magenta
            "\033[96m",  # cyan
        ]
        RESET_COLOR = "\033[0m"

        def get_color(ip):
            if ip not in ip_colors:
                ip_colors[ip] = colors[len(ip_colors) % len(colors)]
            return ip_colors[ip]

        def process_packet(packet):
            global last_packet_time
            last_packet_time = time.time()

            print("\n=== Neues Paket ===")

            if packet.haslayer(IP):
                ip_layer = packet[IP]
                src_color = get_color(ip_layer.src)
                dst_color = get_color(ip_layer.dst)

                print(f"Quelle IP: {src_color}{ip_layer.src}{RESET_COLOR}")
                print(f"Ziel IP:   {dst_color}{ip_layer.dst}{RESET_COLOR}")
                print(f"TTL:       {ip_layer.ttl}")

                if packet.haslayer(TCP):
                    tcp_layer = packet[TCP]
                    print("[TCP]")
                    print(f"Port (src): {tcp_layer.sport}")
                    print(f"Port (dst): {tcp_layer.dport}")
                    print(f"Flags:      {tcp_layer.flags}")

                elif packet.haslayer(UDP):
                    udp_layer = packet[UDP]
                    print("[UDP]")
                    print(f"Port (src): {udp_layer.sport}")
                    print(f"Port (dst): {udp_layer.dport}")

                elif packet.haslayer(ICMP):
                    print("[ICMP] Ping / Netzwerkdiagnose")
            else:
                print("Kein IP Paket erkannt")

        def stop_filter(packet):
            global last_packet_time
            if time.time() - last_packet_time > IDLE_TIMEOUT:
                print("Zeitüberschreitung!")
                return True
            return False

        filteryn = input("IP Filter y/n: ")
        if filteryn.lower() == "y":
            ip_filter = input("IP-Adresse: ")
            sniff(filter=f"host {ip_filter}", prn=process_packet, stop_filter=stop_filter)
        elif filteryn.lower() == "n":
            sniff(prn=process_packet, stop_filter=stop_filter)
        else:
            print("Ungültige Eingabe!")
    case "3":
        ipmapmapper = r"""
 _  ____    _      ____  ____    _      ____  ____  ____  _____ ____ 
/ \/  __\  / \__/|/  _ \/   _\  / \__/|/  _ \/  __\/  __\/  __//  __\
| ||  \/|  | |\/||| / \||  /    | |\/||| / \||  \/||  \/||  \  |  \/|
| ||  __/  | |  ||| |-|||  \__  | |  ||| |-|||  __/|  __/|  /_ |    /
\_/\_/     \_/  \|\_/ \|\____/  \_/  \|\_/ \|\_/   \_/   \____\\_/\_\
                                                                     
                                                                               
        ┌───────────────────────────────────────────────┐
        │        IP → MAC → HOSTNAME RESOLVER           │
        │      Passive Network Discovery Scanner        │
        └───────────────────────────────────────────────┘

                [*] Sniffing Network Traffic...
                [*] Detecting Devices...
                [*] Resolving Hostnames...
"""

        print(ipmapmapper)
        time.sleep(2)
        #IP-MAC Mapper
        from scapy.all import sniff, IP, Ether
        import socket

        # Speicher, um die Konsole nicht mit doppelten Meldungen zu fluten
        seen_devices = set()
        def get_hostname(ip):
            try:
                # Versucht den Namen zur IP zu finden
                hostname = socket.gethostbyaddr(ip)[0]
                return hostname
            except socket.herror:
                # Wenn kein Name im Netzwerk hinterlegt ist
                return "Unbekannt"

        def process_packet(packet):
            if packet.haslayer(IP):
                src_ip = packet[IP].src
                
                # Wir filtern auf dein lokales Netz (z.B. 192.168.), um Internet-Server zu ignorieren
                if src_ip.startswith("192.168.") and src_ip not in seen_devices:
                    
                    # BSSID/MAC extrahieren
                    bssid_mac = packet[Ether].src if packet.haslayer(Ether) else "Nicht gefunden"
                    
                    # Hostnamen abfragen
                    name = get_hostname(src_ip)
                    
                    print(f"[GERÄT GEFUNDEN]")
                    print(f"  IP:       {src_ip}")
                    print(f"  Hostname: {name}")
                    print(f"  BSSID/MAC: {bssid_mac}")
                    print("-" * 30)
                    
                    seen_devices.add(src_ip)
        
        print("Suche im Netzwerk nach Geräten, Namen und BSSIDs...")
        print("(Stelle sicher, dass du das Programm als Administrator gestartet hast)")

        # Sniffe ohne Limit (store=0 spart Arbeitsspeicher)
        sniff(prn=process_packet, store=0)

    case _: 
        print("Ungültige Eingabe")
