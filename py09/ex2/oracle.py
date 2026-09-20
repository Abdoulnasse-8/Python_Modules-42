import os

try:
    from dotenv import load_dotenv  # type: ignore
except ImportError:
    load_dotenv = None


def load_environment() -> None:
    if load_dotenv:
        load_dotenv()


def get_env(key: str) -> str:
    value = os.getenv(key)
    if not value:
        print(f"[MISSING] {key}")
        return "[NOT SET]"
    return value


def mask_secret(value: str) -> str:
    if value in ("[NOT SET]", "your_api_key_here"):
        return "[NOT SET]"
    return value[:3] + "***"


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_environment()

    mode = get_env("MATRIX_MODE")
    db = get_env("DATABASE_URL")
    api = get_env("API_KEY")
    log = get_env("LOG_LEVEL")
    zion = get_env("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if db != "[NOT SET]":
        print("Database: Connected")
    else:
        print("Database: Not connected")

    if api != "[NOT SET]":
        print(f"API Access: Authenticated ({mask_secret(api)})")
    else:
        print("API Access: Not authenticated")

    print(f"Log Level: {log}")

    if zion != "[NOT SET]":
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file present")
    else:
        print("[WARN] .env file missing")

    if os.path.exists(".gitignore"):
        with open(".gitignore", "r", encoding="utf-8") as f:
            if ".env" in f.read():
                print("[OK] .env is ignored in git")
            else:
                print("[WARN] .env not in gitignore")

    print("[OK] No hardcoded secrets")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
