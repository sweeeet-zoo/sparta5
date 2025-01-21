import seaborn as sns
tips = sns.load_dataset('tips')

from google.colab import files
from google.oauth2 import service_account
uploaded = files.upload()

key_path = list(uploaded.keys())[0]
credentials = service_account.Credentials.from_service_account_file(key_path)

from google.cloud import bigquery
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

job = client.load_table_from_dataframe(tips, 'mydataset.tips')
job.result()

# 결과 확인
print(f"Uploaded {job.output_rows} rows to {job.destination}.")
