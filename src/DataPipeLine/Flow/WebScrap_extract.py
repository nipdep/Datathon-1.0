import os
import json
from src.DataPipeLine.Scripts.Helpers.dateformat import *
import luigi
from src.DataPipeLine.Scripts.read_pdf import *
from luigi.contrib import mysqldb
from luigi.util import requires, inherits, common_params

Directory='F:/Deeplearning/Datathon-1.0'
pdf_dir = Directory+'/data/daily_pdf'
log_dir = Directory+'/src/DataPipeLine/Flow/logs'


class WebScrapingExtract(luigi.Task):

    def __init__(self, *args, **kwargs):
        """ something if needed"""
        super().__init__(*args, **kwargs)
        self.current_date = dateformat()
        self.log_file = log_dir+'/'+self.current_date[0]+'-'+self.current_date[1]+'extract.json'

    def requires(self):
        """ Since First Layer not required by anything """

    def output(self):
        """ Output a data but saving file recommended  """
        return luigi.LocalTarget(self.log_file)

    def run(self):
        """ Nipun's web scraping code """
        print(os.path.exists(pdf_dir+'/'+self.current_date[0]+'-'+self.current_date[1]+'.pdf'))
        if(os.path.exists(pdf_dir+'/'+self.current_date[0]+'-'+self.current_date[1]+'.pdf')):
            details = getPDF(pdf_dir+'/'+self.current_date[0]+'-'+self.current_date[1]+'.pdf')
        else:
            print('pdf not exist yet')
            print('pdf path checked :- ',pdf_dir+'/'+self.current_date[0]+'-'+self.current_date[1]+'.pdf')
            details = {'status':'pdf not exist yet',
                       'path_detail':pdf_dir+'/'+self.current_date[0]+'-'+self.current_date[1]+'.pdf'}
        #process

        try:
            with self.output().open(mode='w') as f:
                json.dump(details, f)
        except:
            print('error')
