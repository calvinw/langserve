import requests
def download_csv(url, local_filename):
    """Downloads a CSV file from a URL and saves it to a local file.

    Args:
        url (str): The URL of the CSV file to download.
        local_filename (str): The name of the local file to save the CSV to.

    Returns:
        None
    """

    response = requests.get(url)

    if response.status_code == 200:
        with open(local_filename, "wb") as f:
            f.write(response.content)
        print(f"File downloaded successfully to {local_filename}!")
    else:
        print(f"Download failed: {response.status_code}")

#Download the testing data from google spreadsheet
testingUrl="https://docs.google.com/spreadsheets/d/e/2PACX-1vRKHzmZ7UmKD_DjLbx5tSxIO-3VRyxiGrcs5ZehehZbZJbNwJF4STZDrCfvGEwjsdgQGWl9KafzxwLS/pub?gid=2071210157&single=true&output=csv"
download_csv(testingUrl, "app/test_data.csv")

#Download the training (few shot)data from google spreadsheet
trainingUrl="https://docs.google.com/spreadsheets/d/e/2PACX-1vRKHzmZ7UmKD_DjLbx5tSxIO-3VRyxiGrcs5ZehehZbZJbNwJF4STZDrCfvGEwjsdgQGWl9KafzxwLS/pub?gid=0&single=true&output=csv"
download_csv(trainingUrl, "app/training_data.csv")
