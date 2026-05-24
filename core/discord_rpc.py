from pypresence import Presence


class DiscordRPC:

    def __init__(self):

        self.client_id = "1375948553759852554"

        self.rpc = None

    def start(self):

        try:

            self.rpc = Presence(
                self.client_id
            )

            self.rpc.connect()

            self.rpc.update(
                state="In Launcher",
                details="Nova Launcher",
                large_image="logo",
                large_text="Nova Launcher",
                start=int(__import__("time").time())
            )

            print(
                "Discord RPC started"
            )

        except Exception as error:

            print(
                "RPC Error:",
                error
            )

    def update_playing(
        self,
        nickname,
        version
    ):

        try:

            if self.rpc:

                self.rpc.update(
                    state=f"Playing {version}",
                    details=f"Nickname: {nickname}",
                    large_image="logo",
                    large_text="Nova Launcher",
                    start=int(__import__("time").time())
                )

        except Exception as error:

            print(
                "RPC Update Error:",
                error
            )