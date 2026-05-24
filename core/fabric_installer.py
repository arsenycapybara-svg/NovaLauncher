import minecraft_launcher_lib


class FabricInstaller:

    @staticmethod
    def install(
        version_id,
        minecraft_dir,
        callback=None
    ):

        loader_version = (
            minecraft_launcher_lib.fabric.get_latest_loader_version()
        )

        minecraft_launcher_lib.fabric.install_fabric(
            version_id,
            minecraft_dir,
            loader_version=loader_version,
            callback=callback
        )