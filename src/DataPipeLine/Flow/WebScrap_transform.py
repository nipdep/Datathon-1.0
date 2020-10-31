import os
import json

import luigi
from luigi.contrib import mysqldb
from luigi.util import requires, inherits, common_params


class WebScrapingTransform(luigi.Task):
    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)

    def requires(self):
        """ Since First Layer not required by anything """

    def output(self):
        """ Output a Json file most probably """

    def run(self):
        """ required transforms """
