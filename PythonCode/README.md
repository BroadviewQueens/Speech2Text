Step1:
pip install azure.cognitiveservices.speech

Step2:
pip install azure.storage.blob

Step3:
Change values for below variables-

speech_key, service_region = "Your Speech2Text key", "your region"

AZURE_STORAGE_CONNECTION_STRING="Copy the key here"

container_name ="Give container name of your choice"

inputfilename = "provide the path of audio1.wav"

outputfilename = "speech2text.csv"
