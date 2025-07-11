import subprocess

def main():
    print("=== KeyHunt Launcher ===")

    address = input("Shkruaj Bitcoin adresën: ").strip()
    start = input("Range fillimi (hex, p.sh. 0x4FFFFFFFFFFFFFFF): ").strip()
    end = input("Range fundi (hex, p.sh. 0x7FFFFFFFFFFFFFFFFF): ").strip()
    threads = input("Numri i thread-eve (p.sh. 256): ").strip()

    # Krijo targets.txt
    with open("targets.txt", "wb") as f:
        f.write(address.encode("ascii"))

    print("[+] targets.txt u krijua me sukses.")

    command = [
        "./keyhunt.exe",
        "-m", "bsgs",
        "-f", "targets.txt",
        "-r", f"{start}:{end}",
        "-t", threads,
        "-q"
    ]

    print(f"[+] Nisja e keyhunt.exe me range {start} deri {end}")
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"[!] Gabim: {e}")

if __name__ == "__main__":
    main()
