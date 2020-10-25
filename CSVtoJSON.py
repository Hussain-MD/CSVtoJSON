# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:40:52 2020

@author: Hussain Dhorajiwala
"""

import csv , json,sys,glob,os
import configparser as cp
from datetime import datetime
arr = []
#read the csv and add the arr to a arrayn
        
class CsvToJson():
    def __init__(self,config_file="csvToJson.properties"):
        try:
            config = cp.RawConfigParser()
            config.read(config_file)
            self.csvFilePath =config.get('APPSETTINGS', 'csvFilePath')
        
        except Exception as ex:
            exc_type,exc_obj,exc_tb=sys.exc_info()
            print("Error in __init__ method at {}, Error Message---- {} ".format(exc_tb.tb_lineno,ex))
    
    def writeoutput(self,infilename,logs):
        try:
            """
            Reason: To Write log ,Errors into a file,
            Input : FileName,logs
            Return: 
            """
            with open( infilename +'.txt', 'a') as filehandle:
                filehandle.write('%s\n' % logs.encode('ISO-8859-1').strip())
        except Exception as ex:
            print('writeoutput- error')
            print(ex)
    
    def csvToJsonConversion(self):
        try:
            """
            Reason: To Write log ,Errors into a file,
            Input : FileName,logs
            Return: 
            """
            self.writeoutput("Logger","{}^{}\n".format("Script Start time",str(datetime.now())))

            counter=0
            for csvfile in glob.glob(os.path.join(self.csvFilePath,'*.csv')):
                'Below code will create folder for 1 CSV file'
                
                filename=csvfile.split('\\')[-1][:-4]
                output_folder_path=self.csvFilePath+filename
                print(filename)
                print(output_folder_path)
                try:
                    os.mkdir(output_folder_path)
                except Exception as ex:
                    exc_type,exc_obj,exc_tb=sys.exc_info()
                    print("Error in folder creation {}, Error Message---- {} ".format(exc_tb.tb_lineno,ex))
               

                df_data = pd.read_csv(csvfile)
                df_data["TFMDAT"]= pd.to_datetime(df_data["TFMDAT"],format="%d/%m/%Y",errors="ignore")
                df_data["TFMDAT"]=pd.to_datetime(df_data["TFMDAT"]).map(datetime.strftime("%d-%m-%Y"))
                print(df_data.head())
                csvFile=codecs.open(csvfile, 'rU', 'utf-16'):
                csvReader = csv.DictReader(codecs.open(csvfile, 'rU', 'utf-16'))
                print(csvReader)
                import shutil
                import codecs
                arr=[]
                try:                     
                    with open(csvfile,encoding="utf-8") as csvfile:
                        csv.reader(codecs.open('file.csv', 'rU', 'utf-16'))
                        csvReader = csv.DictReader((line.replace('\x00', '') for line in csvfile))
   			arr.append(csvRow)
                except Exception as e:
                    destination=""
                    errorfile=self.csvFilePath+filename+ ".csv"
                    print(errorfile)
                    shutil.move(errorfile, destination)
                    path=os.path.join(self.csvFilePath,filename)
                    os.rmdir(path)
                    continue

                for i in range(0,len(arr)):
                    
                    arr[i]=dict(arr[i])
                    #print(arr[i])
                    for key in arr[i].keys():
                        if(not isinstance(arr[i][key],float) and not isinstance(arr[i][key],int) and isinstance(arr[i][key],str) and arr[i][key] is not None):
                                         
                            arr[i][key]=arr[i][key].encode('ascii', 'replace').decode('utf-8')
                        
                        dictionary[column_names[j]]=str(list(row[i])[j]).encode('ascii', 'replace').decode('utf-8')

                    filename1=filename+"_"+str(i)+".json"
                    with open(output_folder_path+"\\"+filename1, "w") as jsonFile:
                        jsonFile.write(json.dumps(data, indent = 4))
                    self.writeoutput("Logger","{}^{}^{}^{}^{}\n".format("output_folder_path",output_folder_path,"filename: ",filename1,str(datetime.now())))

                self.writeoutput("Logger","{}^{}\n".format("Script End Time",str(datetime.now())))
               
        except Exception as ex:
            exc_type,exc_obj,exc_tb=sys.exc_info()
            self.writeoutput("Error","{}^{}^{}^{}^{}".format("csvToJsonConversion",self.csvFilePath,str(datetime.now()), exc_tb.tb_lineno ,ex))
            print("Error in csvToJsonConversion method at {}, Error Message---- {} ".format(exc_tb.tb_lineno,ex))        
         
obj=CsvToJson("csvToJson.properties")
obj.csvToJsonConversion()   
  
