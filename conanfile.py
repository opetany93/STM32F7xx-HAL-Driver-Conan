from conans import ConanFile, CMake


class STM32F7xxHALDriverConan(ConanFile):
    name = "STM32F7xx_HAL_Driver"
    version = "1.2.8"
    license = "BSD 3-Clause"
    author = "STMicroelectronics"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "An abstraction drivers layer, the API ensuring maximized portability across the STM32 portfolio"
    generators = "cmake"
    build_policy = "missing"

    def export(self):
        self.copy("*.c", dst="STM32F7xx_HAL/src", src="Src")
        self.copy("*.h", dst="STM32F7xx_HAL/inc", src="Inc")

