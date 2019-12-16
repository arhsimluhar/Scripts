#Copy this code in your first block of cell after updating your values.
import os
os.environ['KAGGLE_USERNAME'] = '<kaggle-user-name>'
os.environ['KAGGLE_KEY'] = '<kaggle-key>'
os.environ['KAGGLE_PROXY'] = '<proxy-address>' 
os.environ['KAGGLE_DATASET'] = '<Kaggle-dataset>'
#setup the my customised environment for google colab
!wget https://raw.githubusercontent.com/rahul1809/Scripts/master/Google-Colab/setup.sh && chmod +x setup.sh && ./setup.sh

#download the kaggle dataset for the competition
!kaggle datasets download -d os.environ["KAGGLE_DATASET"]


