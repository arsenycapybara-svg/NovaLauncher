import json
from pathlib import Path


PROFILES_FILE = Path("profiles/profiles.json")


class ProfileManager:

    def __init__(self):
        PROFILES_FILE.parent.mkdir(exist_ok=True)

        if not PROFILES_FILE.exists():
            self.save_profiles([])

    def load_profiles(self):
        with open(PROFILES_FILE, "r") as f:
            return json.load(f)

    def save_profiles(self, data):
        with open(PROFILES_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_profile(self, nickname):
        profiles = self.load_profiles()

        profiles.append({
            "nickname": nickname
        })

        self.save_profiles(profiles)