from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools
import os

class XSensMTIConan(ConanFile):
    name = "xsens_mti"
    version = "2019.2.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    
    def source(self):
        self.run("git clone https://github.com/Roboauto/conan-xsens_mti_driver.git")
        self.run("cd conan-xsens_mti_driver && git checkout master")
    def build(self):
        with tools.chdir(os.path.join("conan-xsens_mti_driver","xspublic")):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.make()

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join("conan-xsens_mti_driver","xspublic"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [ 'xscontroller', 'xscommon' ,'xstypes']
        
