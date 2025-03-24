from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    'sjleshrac/airlines-customer-satisfaction',
    path='data',
    unzip=True
)

print("✅ Download abgeschlossen!")