#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from os import path


class FakeItConan(ConanFile):
    name = "FakeIt"
    version = "2.0.4"
    generators = "cmake"
    url = "https://github.com/xqp/conan-fakeit"
    author = "Patrik Fiedler <patrik.fiedler@gmail.com>"
    license = "https://github.com/eranpeer/FakeIt/blob/master/LICENSE"
    description = "C++ mocking made easy. A simple yet very expressive, headers only library for c++ mocking."
    options = {"framework": ["boost", "catch", "gtest", "mettle", "mstest", "qtest", "standalone", "tpunit"]}
    default_options = "framework=standalone"
    root = "%s-%s" % (name, version)

    def source(self):
        source_url = "https://github.com/eranpeer/FakeIt"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        
    def package(self):
        self.copy(pattern="fakeit.hpp", dst="include", src=path.join(self.root, "single_header", "{0}".format(self.options.framework)))

    def package_id(self):
        self.info.header_only()
        