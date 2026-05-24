from pathlib import Path
import shutil


class InstanceManager:

    INSTANCES_DIR = Path(
        "instances"
    )

    @classmethod
    def get_instances(cls):

        cls.INSTANCES_DIR.mkdir(
            exist_ok=True
        )

        instances = []

        for folder in cls.INSTANCES_DIR.iterdir():

            if folder.is_dir():

                instances.append(
                    folder.name
                )

        return instances

    @classmethod
    def create_instance(
        cls,
        name
    ):

        instance_path = (
            cls.INSTANCES_DIR / name
        )

        instance_path.mkdir(
            parents=True,
            exist_ok=True
        )

        (instance_path / "mods").mkdir(
            exist_ok=True
        )

        (instance_path / "resourcepacks").mkdir(
            exist_ok=True
        )

        (instance_path / "saves").mkdir(
            exist_ok=True
        )

        return instance_path

    @classmethod
    def delete_instance(
        cls,
        name
    ):

        instance_path = (
            cls.INSTANCES_DIR / name
        )

        if instance_path.exists():

            shutil.rmtree(
                instance_path
            )