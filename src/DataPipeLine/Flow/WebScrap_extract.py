import os
import json

import luigi
from luigi.contrib import mysqldb
from luigi.util import requires, inherits, common_params


class WebScrapingExtract(luigi.Task):

    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)
        self.data = None

    def requires(self):
        """ Since First Layer not required by anything """

    def output(self):
        """ Output a data but saving file recommended  """
        return self.data

    def run(self):
        """ Nipun's web scraping code """


        #process

        return self.output()
