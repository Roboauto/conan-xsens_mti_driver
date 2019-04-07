from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools


class XSensMTIConan(ConanFile):
    name = "xsens_mti"
    version = "2019.0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "xspublic/*"

    def build(self):
        with tools.chdir("xspublic"):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.make()

    def package(self):
        self.copy("*.h", dst="include", src="xspublic")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

