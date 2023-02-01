#!/usr/bin/env python

# SPDX-FileCopyrightText: 2013 SAP SE Srdjan Boskovic <srdjan.boskovic@sap.com>
#
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-

import unittest
import pyrfc

from tests.config import PARAMS as params, PARAMSDEST as paramsdest, CONFIG_SECTIONS as config_sections, LANGUAGES


class TestRfcSDK:
    # def setup_method(self, test_method):
    #     self.conn = pyrfc.Connection(**paramsdest)
    #     assert self.conn.alive

    # def teardown_method(self, test_method):
    #     self.conn.close()
    #     assert not self.conn.alive

    def test_version(self):
        with open("VERSION", "r") as f:
            VERSION = f.read().strip()
            assert pyrfc.__version__ == VERSION

    def test_reload_ini_file(self):
        pyrfc.reload_ini_file()
        # no errors expected
        assert 1 == 1

    def test_language_iso_sap(self):
        for lang_iso in LANGUAGES:
            lang_sap = pyrfc.language_iso_to_sap(lang_iso)
            assert lang_sap == LANGUAGES[lang_iso]["lang_sap"]

            laiso = pyrfc.language_sap_to_iso(lang_sap)
            assert laiso == lang_iso


if __name__ == "__main__":
    unittest.main()