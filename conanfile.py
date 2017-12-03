from conans import ConanFile, tools

class VariantliteConan(ConanFile):
    name = "variant-lite"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/martinmoene/variant-lite"
    description = "A single-file header-only version of a C++17-like variant, a type-safe union for C++98, C++11 and later"

    def source(self):
        self.run("git clone https://github.com/martinmoene/variant-lite.git")
        self.run("cd variant-lite && git checkout 9c34c9b0f19b6f4ccdf2c46635c4f9510c13dd27")

    def package(self):
        self.copy(pattern="variant.hpp", src="variant-lite/include/nonstd", dst="include", keep_path=False)
