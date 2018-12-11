#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class GradleConan(ConanFile):
    name = "gradle"
    version = "4.10.2"
    url = "https://github.com/Tereius/conan-gradle"
    homepage = "https://gradle.org/"
    description = "Gradle is an open-source build automation tool focused on flexibility and performance."
    license = "https://github.com/gradle/gradle/blob/master/LICENSE"
    build_requires = "java_installer/8.0.144@tereius/stable"
    settings = {"os_build": ["Windows", "Linux", "Macos"]}

    def source(self):
        source_url =\
            "https://downloads.gradle.org/distributions/gradle-%s-bin.zip" % self.version
        tools.get(source_url)

    def package(self):
        self.copy(pattern="*", src="gradle-%s" % self.version)

    def package_info(self):

        ant_root = self.package_folder
        self.output.info('Adding gradle binaries to PATH: %s' % os.path.join(ant_root, "bin"))
        self.env_info.PATH.append(os.path.join(ant_root, "bin"))
