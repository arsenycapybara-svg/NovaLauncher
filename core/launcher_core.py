from pathlib import Path
import subprocess

import minecraft_launcher_lib

from core.config_manager import ConfigManager
from core.java_installer import JavaInstaller


class LauncherCore:

    def __init__(self):

        self.minecraft_dir = Path(
            "minecraft"
        )

        self.minecraft_dir.mkdir(
            exist_ok=True
        )

    # ====================================
    # INSTALL VERSION
    # ====================================

    def install_version(
        self,
        version,
        callback=None
    ):

        minecraft_launcher_lib.install.install_minecraft_version(

            version,

            str(self.minecraft_dir),

            callback=callback
        )

    # ====================================
    # LAUNCH GAME
    # ====================================

    def launch_game(
        self,
        version,
        nickname
    ):

        config = ConfigManager.load()

        # ====================================
        # JAVA
        # ====================================

        if not JavaInstaller.is_java_installed():

            JavaInstaller.install_java()

        java_path = (
            JavaInstaller.get_java_path()
        )

        # ====================================
        # RAM
        # ====================================

        ram = config.get(
            "ram",
            "4G"
        )

        # ====================================
        # JVM ARGS
        # ====================================

        jvm_args = [

            f"-Xmx{ram}",

            f"-Xms{ram}",

            "-XX:+UnlockExperimentalVMOptions",

            "-XX:+UseG1GC"
        ]

        # ====================================
        # AUTHLIB-INJECTOR
        # ====================================

        authlib_path = Path(
            "authlib-injector.jar"
        )

        if authlib_path.exists():

            jvm_args.append(
                f"-javaagent:{authlib_path}=https://ely.by"
            )

            print(
                "[ELY.BY] authlib-injector enabled"
            )

        else:

            print(
                "[ELY.BY] authlib-injector.jar not found"
            )

        # ====================================
        # OPTIONS
        # ====================================

        options = {

            "username": nickname,

            "uuid": "00000000000000000000000000000000",

            "token": "",

            "jvmArguments": jvm_args,

            "gameDirectory": str(
                self.minecraft_dir
            )
        }

        # ====================================
        # CHECK VERSION
        # ====================================

        version_path = (
            self.minecraft_dir
            / "versions"
            / version
        )

        jar_file = (
            version_path
            / f"{version}.jar"
        )

        json_file = (
            version_path
            / f"{version}.json"
        )

        if not jar_file.exists() or not json_file.exists():

            raise Exception(
                "Version is not installed fully"
            )

        # ====================================
        # COMMAND
        # ====================================

        command = minecraft_launcher_lib.command.get_minecraft_command(

            version,

            str(self.minecraft_dir),

            options
        )

        # ====================================
        # CUSTOM JAVA
        # ====================================

        command[0] = java_path

        # ====================================
        # DEBUG
        # ====================================

        print("\n".join(command))

        # ====================================
        # START GAME
        # ====================================

        subprocess.Popen(
            command
        )