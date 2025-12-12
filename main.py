import time
import random
import sys
import os
import string
import threading
import math
from datetime import datetime

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
BLINK = '\033[5m'

COMMON_PORTS = [
    (21, "FTP"), (22, "SSH"), (23, "TELNET"), (25, "SMTP"), (53, "DNS"),
    (80, "HTTP"), (110, "POP3"), (135, "RPC"), (139, "NETBIOS"), (143, "IMAP"),
    (443, "HTTPS"), (445, "SMB"), (993, "IMAPS"), (995, "POP3S"), (1433, "MSSQL"),
    (3306, "MYSQL"), (3389, "RDP"), (5900, "VNC"), (8080, "HTTP-PROXY")
]

USER_AGENTS = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    "Dalvik/2.1.0 (Linux; U; Android 11; Pixel 5 Build/RQ3A.211001.001)",
    "Cyberdeck/9.0 (NeuroLink; Latency 0ms) RootAccess/1.0"
]

PASSWORDS = [
    "admin", "password", "123456", "root", "qwerty", "master", "letmein",
    "dragon", "baseball", "mustang", "shadow", "superman", "jordan", "michael",
    "access", "database", "system", "cisco", "oracle", "secret", "god", "angel",
    "trustno1", "hacker", "l33t", "hunter2", "iloveyou", "princess", "rockstar"
]

USERNAMES = [
    "admin", "root", "user", "guest", "info", "adm", "mysql", "user1",
    "administrator", "oracle", "ftp", "test", "support", "sys", "server"
]

DIRS = [
    "/var/www/html", "/etc/shadow", "/home/root", "/usr/local/bin",
    "/opt/secret", "/tmp/cache", "/var/log/auth.log", "/dev/null",
    "/sys/kernel/security", "/proc/net/tcp", "/boot/efi"
]

SQL_QUERIES = [
    "SELECT * FROM users WHERE admin=1;",
    "DROP TABLE logs;",
    "UNION SELECT user, password FROM credit_cards;",
    "UPDATE accounts SET balance = 0 WHERE id = 99;",
    "INSERT INTO shell_code (payload) VALUES (0x909090);",
    "DELETE FROM firewall_rules WHERE active=1;"
]

class System:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    @staticmethod
    def random_ip():
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

    @staticmethod
    def random_mac():
        return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])

    @staticmethod
    def type_out(text, speed=0.01, color=GREEN, end="\n"):
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(RESET + end)

    @staticmethod
    def banner():
        art = f"""
{RED}        .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                     __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   {WHITE}DIE{RED}    `98v8P'  {WHITE}DIE{RED}   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
{RESET}"""
        System.clear()
        print(art)
        System.sleep(1)

class ModuleNetworkScanner:
    def run(self, duration=10):
        System.clear()
        print(f"{CYAN}{BOLD}[*] INITIATING ADVANCED PORT SCANNER v4.0{RESET}")
        print(f"{DIM}TARGET SCOPE: GLOBAL{RESET}\n")
        
        start_time = time.time()
        while time.time() - start_time < duration:
            ip = System.random_ip()
            port_info = random.choice(COMMON_PORTS)
            status = random.choice([f"{GREEN}OPEN{RESET}", f"{RED}CLOSED{RESET}", f"{YELLOW}FILTERED{RESET}"])
            
            sys.stdout.write(f"\r{WHITE}SCANNING {ip} ... {RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
            
            if "OPEN" in status:
                print(f"\r{GREEN}[+] FOUND: {ip}:{port_info[0]} ({port_info[1]}) >> SERVICE EXPOSED{RESET}")
                time.sleep(0.1)
            elif random.random() > 0.9:
                print(f"\r{RED}[-] {ip} : HOST UNREACHABLE (Packet Loss 100%){RESET}")
        
        print(f"\n{BOLD}{CYAN}>>> NETWORK SCAN COMPLETE. 403 VULNERABILITIES INDEXED.{RESET}")
        time.sleep(2)

class ModuleBruteForce:
    def run(self, duration=10):
        System.clear()
        print(f"{RED}{BOLD}[!] INITIATING DICTIONARY ATTACK PROTOCOL{RESET}")
        target = f"admin@{System.random_ip()}"
        print(f"{YELLOW}TARGET: {target}{RESET}\n")
        
        start_time = time.time()
        attempts = 0
        
        while time.time() - start_time < duration:
            attempts += 1
            user = random.choice(USERNAMES)
            pwd = random.choice(PASSWORDS)
            
            if random.random() > 0.5:
                pwd += str(random.randint(0, 999))
                
            sys.stdout.write(f"\r{DIM}[{attempts}] TRYING: {user}:{pwd} ... {RESET}")
            sys.stdout.flush()
            time.sleep(0.01)
            
            if random.random() > 0.98:
                print(f"\r{RED}[!] FAILED AUTH: {user}:{pwd} (Response: 401 Unauthorized){RESET}")
                
        print(f"\n\n{GREEN}{BOLD}>>> MATCH FOUND: admin:hunter2{RESET}")
        print(f"{GREEN}>>> ACCESS TOKEN GENERATED.{RESET}")
        time.sleep(2)

class ModuleCryptoMiner:
    def run(self, duration=10):
        System.clear()
        print(f"{YELLOW}{BOLD}[$] XMR-STAK-RX CPU MINER v10.4.2{RESET}")
        print(f"{DIM}CONNECTED TO POOL: stratum+tcp://xmr.pool.minergate.com:45700{RESET}\n")
        
        hashrate = 0.0
        start_time = time.time()
        
        while time.time() - start_time < duration:
            hashrate = random.uniform(4500.0, 9800.0)
            temp = random.randint(60, 95)
            power = random.randint(100, 250)
            
            color = GREEN
            if temp > 80: color = YELLOW
            if temp > 90: color = RED
            
            print(f"{color}[CPU0] {hashrate:.2f} H/s | {temp}°C | {power}W | BEST: {random.randint(10000,999999)}{RESET}")
            
            if random.random() > 0.9:
                print(f"{BOLD}{GREEN}[*] RESULT ACCEPTED BY POOL! (Diff: {random.randint(100000, 500000)}){RESET}")
            
            time.sleep(0.2)
            
        print(f"\n{YELLOW}{BOLD}>>> MINING PAUSED. WALLET BALANCE: 4.20394 BTC{RESET}")
        time.sleep(2)

class ModuleDataDump:
    def run(self, duration=8):
        System.clear()
        print(f"{GREEN}{BOLD}SYSTEM DUMP INITIATED...{RESET}\n")
        
        start_time = time.time()
        while time.time() - start_time < duration:
            offset = random.randint(0, 0xFFFF)
            hex_data = " ".join([f"{random.randint(0, 255):02X}" for _ in range(16)])
            ascii_data = "".join([random.choice(string.ascii_letters + ".") for _ in range(16)])
            
            print(f"{GREEN}0x{offset:08X}  {hex_data}  |{ascii_data}|{RESET}")
            time.sleep(0.02)
        
        print(f"\n{GREEN}>>> DUMP SAVED TO /dev/sdb1{RESET}")
        time.sleep(1)

class ModuleMatrixRain:
    def run(self, duration=8):
        System.clear()
        columns = 100
        drops = [0 for _ in range(columns)]
        
        start_time = time.time()
        while time.time() - start_time < duration:
            line = ""
            for i in range(columns):
                if drops[i] > 0:
                    line += f"{GREEN}{random.choice(string.ascii_letters + string.digits)}{RESET}"
                    drops[i] -= 1
                else:
                    if random.random() > 0.95:
                        drops[i] = random.randint(5, 20)
                        line += f"{WHITE}{random.choice(string.ascii_letters)}{RESET}"
                    else:
                        line += " "
            print(line)
            time.sleep(0.05)
        
        time.sleep(1)

class ModuleBioMetrics:
    def run(self, duration=10):
        System.clear()
        print(f"{RED}{BOLD}SUBJECT #8940-A TELEMETRY LINK{RESET}")
        print(f"{DIM}STATUS: CRITICAL STRESS{RESET}\n")
        
        start_time = time.time()
        bpm = 60
        
        while time.time() - start_time < duration:
            bpm += random.randint(-2, 5)
            bp_sys = 120 + (bpm - 60)
            bp_dia = 80 + (bpm - 60)//2
            
            ecg = ""
            for _ in range(20):
                val = random.randint(0, 5)
                if val == 0: ecg += "_"
                elif val == 1: ecg += "/"
                elif val == 2: ecg += "\\"
                elif val == 3: ecg += "^"
                elif val == 4: ecg += "v"
                else: ecg += "-"
                
            print(f"{RED}HR: {bpm} BPM | BP: {bp_sys}/{bp_dia} | O2: {random.randint(95,100)}% | BRAIN: {ecg}{RESET}")
            
            if bpm > 140:
                print(f"{BOLD}{BLINK}{RED}>>> WARNING: CARDIAC ARREST IMMINENT{RESET}")
            
            time.sleep(0.2)
        
        print(f"\n{RED}>>> LINK LOST.{RESET}")
        time.sleep(2)

class ModuleDroneControl:
    def run(self, duration=10):
        System.clear()
        print(f"{CYAN}{BOLD}UAV-77 PREDATOR INTERFACE{RESET}")
        print(f"{DIM}ENCRYPTION: MIL-SPEC AES-256{RESET}\n")
        
        start_time = time.time()
        alt = 15000
        speed = 400
        
        drone_art = r"""
            /\\
           /  \\
          /    \\
         /______\\
        """
        
        while time.time() - start_time < duration:
            alt += random.randint(-50, 50)
            speed += random.randint(-10, 10)
            lat = 33.0 + random.random()
            lon = 44.0 + random.random()
            
            print(f"\033[H\033[J") 
            print(f"{CYAN}{BOLD}UAV-77 PREDATOR INTERFACE{RESET}")
            print(f"{CYAN}{drone_art}{RESET}")
            print(f"{GREEN}---------------------------------------{RESET}")
            print(f"{GREEN}ALTITUDE : {alt} ft{RESET}")
            print(f"{GREEN}AIRSPEED : {speed} kts{RESET}")
            print(f"{GREEN}HEADING  : {random.randint(0,359)} DEG{RESET}")
            print(f"{GREEN}GPS      : {lat:.5f} N, {lon:.5f} E{RESET}")
            print(f"{GREEN}FUEL     : {random.randint(40,60)}%{RESET}")
            print(f"{GREEN}WEAPONS  : {RED}ARMED (HELLFIRE x2){RESET}")
            print(f"{GREEN}TARGET   : {RED}LOCKED{RESET}")
            print(f"{GREEN}---------------------------------------{RESET}")
            
            print(f"\n{YELLOW}TERRAIN RADAR:{RESET}")
            terrain = "".join([random.choice([" ", ".", ",", "_", "n", "A"]) for _ in range(60)])
            print(f"{YELLOW}[{terrain}]{RESET}")
            
            time.sleep(0.2)
        
        print(f"\n{RED}>>> CONNECTION JAMMED.{RESET}")
        time.sleep(2)

class ModuleChatIntercept:
    def run(self, duration=10):
        System.clear()
        print(f"{MAGENTA}{BOLD}[*] SIGNAL INTERCEPTED: ENCRYPTED CHANNEL 9{RESET}")
        print(f"{DIM}DECRYPTING REAL-TIME...{RESET}\n")
        
        users = ["Neo", "Morpheus", "Trinity", "Cypher", "AgentSmith"]
        convos = [
            "The payload is ready.",
            "Are we secure?",
            "They are tracing the line.",
            "I need an exit.",
            "Upload the virus now.",
            "The code is 993-221-001.",
            "Knock knock.",
            "Follow the white rabbit.",
            "System failure imminent.",
            "Blue pill or red pill?"
        ]
        
        start_time = time.time()
        while time.time() - start_time < duration:
            u = random.choice(users)
            m = random.choice(convos)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            print(f"{DIM}[{timestamp}]{RESET} {MAGENTA}<{u}>{RESET} {WHITE}{m}{RESET}")
            
            time.sleep(random.uniform(0.5, 2.0))
            
            if random.random() > 0.7:
                garbage = "".join([random.choice(string.printable) for _ in range(30)])
                print(f"{DIM}[{timestamp}]{RESET} {RED}<ENCRYPTED>{RESET} {DIM}{garbage}{RESET}")
                time.sleep(0.5)

        print(f"\n{RED}>>> CHANNEL CLOSED BY REMOTE HOST.{RESET}")
        time.sleep(2)

class ModuleSQLInjection:
    def run(self, duration=8):
        System.clear()
        print(f"{BLUE}{BOLD}[SQLMAP] AUTOMATED INJECTION TOOL v1.4{RESET}")
        target = "http://finance.corp.global/login.php?id=1"
        print(f"{BLUE}TARGET: {target}{RESET}\n")
        
        start_time = time.time()
        while time.time() - start_time < duration:
            query = random.choice(SQL_QUERIES)
            print(f"{WHITE}[*] TESTING PAYLOAD: {CYAN}{query}{RESET}")
            time.sleep(0.3)
            
            if random.random() > 0.7:
                print(f"{GREEN}[+] VULNERABILITY CONFIRMED: Blind Boolean Based{RESET}")
                print(f"{DIM}    Retrieving schema...{RESET}")
                time.sleep(0.5)
                cols = ["id", "user", "pass", "email", "ssn", "cc_num"]
                print(f"{GREEN}    COLUMNS: {', '.join(cols)}{RESET}")
            else:
                print(f"{RED}[-] PAYLOAD FAILED{RESET}")
                
            time.sleep(0.2)
        
        print(f"\n{BLUE}>>> DATABASE DUMP COMPLETE.{RESET}")
        time.sleep(2)

class ModuleGlobalMap:
    def run(self, duration=5):
        System.clear()
        world_map = [
            "           . _..::__:  ,- -._        ",
            "   _.__   _ _ .--'      ' '  `-._    ",
            " .'  `--'  '               `  '  `   ",
            "|      USA      EUROPE      RUSSIA   |",
            "|   [TARGET]     [HUB]      [PROXY]  |",
            " .     South   _ . -- .       asia   .",
            "   `._Amer_.-'         `-._  __ . '  ",
            "                              '      "
        ]
        
        print(f"{YELLOW}{BOLD}GLOBAL THREAT MAP{RESET}\n")
        for line in world_map:
            print(f"{CYAN}{line}{RESET}")
        
        print("\n")
        start_time = time.time()
        while time.time() - start_time < duration:
            city = random.choice(["NYC", "LDN", "PAR", "MOS", "BEI", "TOK", "SYD", "RIO"])
            threat_level = random.choice(["LOW", "MED", "HIGH", "CRITICAL"])
            color = GREEN
            if threat_level == "MED": color = YELLOW
            if threat_level == "HIGH": color = RED
            if threat_level == "CRITICAL": color = BLINK + RED
            
            print(f"{WHITE}MONITORING NODE: {city} >> THREAT LEVEL: {color}{threat_level}{RESET}")
            time.sleep(0.5)
            
        time.sleep(1)

class ModuleCompiler:
    def run(self, duration=6):
        System.clear()
        print(f"{WHITE}{BOLD}GCC COMPILER v9.3.0 - LINUX X86_64{RESET}")
        print(f"{DIM}MAKEFILE: /usr/src/exploit/Makefile{RESET}\n")
        
        files = ["buffer_overflow.c", "heap_spray.c", "shellcode.asm", "network_layer.h", "encryption.c"]
        
        for f in files:
            print(f"{WHITE}gcc -c {f} -o {f.split('.')[0]}.o -O3 -Wall{RESET}")
            time.sleep(0.5)
            if random.random() > 0.5:
                print(f"{YELLOW}{f}:42: warning: implicit declaration of function 'memcpy'{RESET}")
            
        print(f"\n{GREEN}Linking objects...{RESET}")
        time.sleep(1)
        print(f"{GREEN}Strip symbols...{RESET}")
        time.sleep(0.5)
        print(f"{BOLD}{GREEN}>>> BUILD SUCCESSFUL: ./exploit_final{RESET}")
        time.sleep(2)

class OmniCyberDeck:
    def __init__(self):
        self.modules = [
            ModuleNetworkScanner(),
            ModuleBruteForce(),
            ModuleCryptoMiner(),
            ModuleMatrixRain(),
            ModuleDataDump(),
            ModuleBioMetrics(),
            ModuleDroneControl(),
            ModuleChatIntercept(),
            ModuleSQLInjection(),
            ModuleGlobalMap(),
            ModuleCompiler()
        ]
        self.running = True

    def boot_sequence(self):
        System.clear()
        print(f"{WHITE}OMNI-BOOT LOADER v2.1")
        print(f"Memory Test: {GREEN}64GB OK{RESET}")
        System.sleep(0.5)
        print(f"CPU: {GREEN}128 CORES DETECTED{RESET}")
        System.sleep(0.5)
        print(f"Mounting Volumes: {GREEN}/root [OK], /home [OK], /var [OK]{RESET}")
        System.sleep(0.5)
        print(f"\n{BOLD}{GREEN}SYSTEM READY.{RESET}")
        System.sleep(1)
        System.banner()
        System.type_out(f"{BOLD}WELCOME, OPERATOR.{RESET}", speed=0.05)
        System.sleep(1)

    def interactive_menu(self):
        while True:
            System.clear()
            print(f"{BOLD}{GREEN}=== OMNI-HACKER V9000 MAIN MENU ==={RESET}")
            print(f"{CYAN}1.  AUTO-PILOT (Random Chaos Mode){RESET}")
            print(f"{CYAN}2.  NETWORK SCANNER{RESET}")
            print(f"{CYAN}3.  PASSWORD CRACKER{RESET}")
            print(f"{CYAN}4.  CRYPTO MINER{RESET}")
            print(f"{CYAN}5.  MATRIX RAIN{RESET}")
            print(f"{CYAN}6.  DATA DUMP{RESET}")
            print(f"{CYAN}7.  BIO-METRICS{RESET}")
            print(f"{CYAN}8.  DRONE UPLINK{RESET}")
            print(f"{CYAN}9.  CHAT INTERCEPT{RESET}")
            print(f"{CYAN}10. SQL INJECTOR{RESET}")
            print(f"{CYAN}11. GLOBAL THREAT MAP{RESET}")
            print(f"{CYAN}12. EXPLOIT COMPILER{RESET}")
            print(f"{RED}0.  EXIT SYSTEM{RESET}")
            print(f"{GREEN}====================================={RESET}")
            
            choice = input(f"{BOLD}{WHITE}SELECT MODULE >> {RESET}")
            
            if choice == '1':
                self.chaos_mode()
            elif choice == '2': ModuleNetworkScanner().run()
            elif choice == '3': ModuleBruteForce().run()
            elif choice == '4': ModuleCryptoMiner().run()
            elif choice == '5': ModuleMatrixRain().run()
            elif choice == '6': ModuleDataDump().run()
            elif choice == '7': ModuleBioMetrics().run()
            elif choice == '8': ModuleDroneControl().run()
            elif choice == '9': ModuleChatIntercept().run()
            elif choice == '10': ModuleSQLInjection().run()
            elif choice == '11': ModuleGlobalMap().run()
            elif choice == '12': ModuleCompiler().run()
            elif choice == '0':
                System.type_out(f"\n{RED}SHUTTING DOWN...", 0.1)
                sys.exit()
            else:
                pass

    def chaos_mode(self):
        try:
            while True:
                mod = random.choice(self.modules)
                duration = random.randint(5, 12)
                mod.run(duration)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    try:
        sys.setrecursionlimit(2000)
        deck = OmniCyberDeck()
        deck.boot_sequence()
        deck.interactive_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}FORCED EXIT{RESET}")