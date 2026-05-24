import minecraft_launcher_lib


class ForgeInstaller:

    @staticmethod
    def install(
        version_id,
        minecraft_dir,
        callback=None
    ):

        forge_version = (
            minecraft_launcher_lib.forge.find_forge_version(
                version_id
            )
        )

        minecraft_launcher_lib.forge.install_forge_version(
            forge_version,
            minecraft_dir,
            callback=callback
        )