Folder Structure:
$|_src	|_DataPipeLine|_ BatchCommands 		>> *.bat files [ batch script to run with jenkins]
	|	      |
	|	      |_ FLow          		>> *.py files [ python files which execute by jenkins]
	|	      |
	|	      |_ Scripts|_ Helpers      >> *.py files [ support functions to web scraping and formatting.]
	|	      	        |_ ./           >> *.py files [ web scraping and .csv file updating files]
	|	      
	|_Logs        |_ ./ 			>> apparently empty folder [ use to save log files of the trained models.]
	|						_ get empty by setting it in .gitignore
	|	
	|_models      |_ geo_sub_model |_ panel_analysis.ipynb  >> use to identify fixed effect of labels.
	|             |                |
	|			       |_ LOO_tree_model.ipynb      >> ML_model that trains on global dataset.
	|			       |
	|			       |_ preporcess_test.ipynb     >> pre-process global dataset, that use to train LOO_tree_model
	|                              |
	|			       |_ geo_panel_analysis.ipynb  >> empty file
	|
	|	      |_ main_model    |_ ARIMA.ipynb               >> basic implementation and parameter tuning of ARIMA model
	|			       | 
	|			       |_final_data_cleaning.ipynb  >> time base melting & mapping for final feature tables
	|			       |
	|			       |_final_data_cleaning.ipynb  >> geographical base melting & mapping for final feature tables
	|			       |
	|			       |_main_pipeline.ipynb        >> # *complete pipeline with prediction generating*
	|			       |
	|			       |_pipeline_2.ipynb           >> geographical base feature pre-processing
	|			       |
	|			       |_pipelining_1.ipynb         >> time base feature pre-processing
	|			       |
	|			       |_randomforestclassifier_with_sklearn_pipeline.py >> basic implementation of random forrest regressor
	|			       |
	|			       |_RandomForrest.ipynb        >> regressor parameter tuning file
	|			       |
	|			       |_RFR_with_walking_forward_reg.ipynb >> basic implementation of walking forward cv schema
	|			       |
	|			       |_RUN.py                     >> auto-executing file by jenkins
	|			       |
	|			       |_time_variency_analysis.ipynb >> $neglible
	|			       |
	|			       |_timeseries-forecasting-of-covid-19-arima >> $neglible
	|
	|	     |_sup             |_ support files and testing file for model building and data extraction












   