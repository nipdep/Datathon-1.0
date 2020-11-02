import os
import json
from src.DataPipeLine.Flow.WebScrap_extract import *
import luigi
from luigi.contrib import mysqldb
from luigi.util import requires, inherits, common_params

Directory = 'F:/Deeplearning/Datathon-1.0'
pdf_dir = Directory + '/data/daily_pdf'
log_dir = Directory + '/src/DataPipeLine/Flow/logs'


class WebScrapingTransform(luigi.Task):
    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)
        self.current_date = dateformat()
        self.log_file = log_dir + '/' + self.current_date[0] + '-' + self.current_date[1] + 'transform.json'

    def requires(self):
        """ Since First Layer not required by anything """
        return WebScrapingExtract()

    def output(self):
        """ Output a Json file most probably """
        return luigi.LocalTarget(self.log_file)

    def run(self):
        """ required transforms """

        """ APPLY TRANSFORM IF ANY """
        details = {'status': 'no transforms yet'}

        try:
            with self.output().open(mode='w') as f:
                json.dump(details, f)
        except:
            print('error')
