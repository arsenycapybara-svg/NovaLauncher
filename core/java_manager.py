import shutil


class JavaManager:

    @staticmethod
    def find_java():

        java_path = shutil.which("java")

        if java_path:
            return java_path

        return "Java not found"