# BOSS CYBERSECURITY TOOLKIT v13 - FINAL
# Creator: silviomagno86-netizen
# Location: Dili, Timor-Leste - HP Only
# Score: 92/100 - Level 13

import hashlib, socket, random, base64
import datetime

def banner():
    print("="*55)
    print(" BOSS CYBERSECURITY TOOLKIT v13.0")
    print(" Score 92/100 | Dili Timor-Leste | HP Only")
    print(" Creator: silviomagno86-netizen")
    print(" GitHub: github.com/silviomagno86-netizen")
    print("="*55)
    print(f" Date: {datetime.datetime.now()}")

def hash_tool():
    print("\n--- HASH GENERATOR ---")
    t=input("Masukkan teks: ")
    print(f" MD5: {hashlib.md5(t.encode()).hexdigest()}")
    print(f" SHA1: {hashlib.sha1(t.encode()).hexdigest()}")
    print(f" SHA256: {hashlib.sha256(t.encode()).hexdigest()}")

def port_scan():
    print("\n--- PORT SCANNER ---")
    target=input("Target IP (contoh 8.8.8.8): ")
    for port in [21,22,80,443,8080]:
        s=socket.socket()
        s.settimeout(1)
        try:
            s.connect((target,port))
            print(f" Port {port}: OPEN")
            s.close()
        except:
            print(f" Port {port}: closed")

def pass_gen():
    print("\n--- PASSWORD GENERATOR ---")
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    length=int(input("Panjang (12): ") or "12")
    pwd="".join(random.choice(chars) for _ in range(length))
    print(f" Password: {pwd}")

def ip_info():
    print("\n--- IP INFO ---")
    host=input("Hostname (google.com): ")
    try:
        ip=socket.gethostbyname(host)
        print(f" IP {host}: {ip}")
    except:
        print(" Gagal resolve")

def b64_tool():
    print("\n--- BASE64 ---")
    print("[1] Encode [2] Decode")
    p=input("Pilih: ")
    if p=="1":
        t=input("Teks: ")
        print(base64.b64encode(t.encode()).decode())
    else:
        t=input("Base64: ")
        print(base64.b64decode(t.encode()).decode())

def main():
    banner()
    while True:
        print("\n--- MENU 10 TOOLS ---")
        print("[1]Hash [2]PortScan [3]PassGen [4]IP Info [5]Base64")
        print("[6]Whois [7]Headers [8]Crack [9]Subdomain [10]VulnCheck")
        print("[0]Keluar")
        c=input("Pilih boss: ")
        if c=="0":
            print("Salam dari Dili! Timor-Leste maju!")
            break
        elif c=="1": hash_tool()
        elif c=="2": port_scan()
        elif c=="3": pass_gen()
        elif c=="4": ip_info()
        elif c=="5": b64_tool()
        else:
            print(f" Tool {c} - Coming soon! Score 92/100 aktif")

if __name__=="__main__":
    main()
