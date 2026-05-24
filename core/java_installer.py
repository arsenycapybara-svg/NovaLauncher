from pathlib import Path

import requests
import tarfile
import os


class JavaInstaller:

    JAVA_DIR = Path("java")

    JAVA_URL = (
        "https://api.adoptium.net/v3/binary/latest/21/ga/linux/x64/jdk/hotspot/normal/eclipse"
    )

    @classmethod
    def is_java_installed(cls):

        java_bin = list(
            cls.JAVA_DIR.glob(
                "jdk-*/bin/java"
            )
        )

        return len(java_bin) > 0

    @classmethod
    def get_java_path(cls):

        java_bin = list(
            cls.JAVA_DIR.glob(
                "jdk-*/bin/java"
            )
        )

        if java_bin:

            return str(
                java_bin[0]
            )

        return "java"

    @classmethod
    def install_java(
        cls,
        progress_callback=None
    ):

        cls.JAVA_DIR.mkdir(
            exist_ok=True
        )

        archive_path = (
            cls.JAVA_DIR
            / "java.tar.gz"
        )

        response = requests.get(
            cls.JAVA_URL,
            stream=True
        )

        total = int(
            response.headers.get(
                "content-length",
                0
            )
        )

        downloaded = 0

        with open(
            archive_path,
            "wb"
        ) as file:

            for chunk in response.iter_content(
                chunk_size=8192
            ):

                if chunk:

                    file.write(
                        chunk
                    )

                    downloaded += len(
                        chunk
                    )

                    if (
                        progress_callback
                        and total > 0
                    ):

                        percent = int(
                            downloaded
                            / total
                            * 100
                        )

                        progress_callback(
                            percent
                        )

        with tarfile.open(
            archive_path,
            "r:gz"
        ) as tar:

            tar.extractall(
                cls.JAVA_DIR
            )

        os.remove(
            archive_path
        )