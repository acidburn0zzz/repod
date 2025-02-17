from pathlib import Path

DB_USER = "root"
DB_GROUP = "root"
DB_FILE_MODE = "0644"
DB_DIR_MODE = "0755"
ARCHITECTURES = ["aarch64", "arm", "armv6h", "armv7h", "i486", "i686", "pentium4", "riscv32", "riscv64", "x86_64"]
SETTINGS_LOCATION = Path("/etc/repod.conf")
SETTINGS_OVERRIDE_LOCATION = Path("/etc/repod.conf.d/")
PACKAGE_REPO_BASE = Path("/var/lib/repod/repo")
SOURCE_REPO_BASE = Path("/var/lib/repod/source")

MANAGEMENT_REPO = Path("/var/lib/repod/management/default")
PACKAGE_POOL = Path("/var/lib/repod/pool/package/default")
SOURCE_POOL = Path("/var/lib/repod/pool/source/default")
