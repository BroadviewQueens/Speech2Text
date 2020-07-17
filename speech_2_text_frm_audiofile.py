# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:16:27 2020

@author: amanm
"""


#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech recognition samples for the Microsoft Cognitive Services Speech SDK
"""

import time
import wave
import os
import sys
import pandas as pd
from azure.storage.blob import BlobServiceClient

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "8fe4ff90e44d4e65a8f2836000aff137", "eastus"
AZURE_STORAGE_CONNECTION_STRING='DefaultEndpointsProtocol=https;AccountName=trainstorage2020;AccountKey=s4cx8Io6R6dYD4V+9iqCqTwHufFqWDnxFN8FXrYOH0Da7o5qrE+uuMR9Fj4z5bXmO9+CcKNH5JovqkyhD7kT/g==;EndpointSuffix=core.windows.net'
container_name='testcon'
# Specify the path to an audio file containing speech (mono WAV / PCM with a sampling rate of 16
# kHz).
inputfilename = "C:/Swadesh/MMAI/MMAI 844/training/audio1.wav"
outputfilename = "speech2text.csv"

def speech_recognize_once_from_mic():
    """performs one-shot speech recognition from the default microphone"""
    print("performs one-shot speech recognition from the default microphone")
    # <SpeechRecognitionWithMicrophone>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Creates a speech recognizer using microphone as audio input.
    # The default language is "en-us".
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    print("Say something...")
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    # </SpeechRecognitionWithMicrophone>
    file1 = open("audiofile_to_text.txt","w")
    file1.write(result.text)
    file1.close()
    
    try:
        CONNECTION_STRING = AZURE_STORAGE_CONNECTION_STRING

    except KeyError:
        print("AZURE_STORAGE_CONNECTION_STRING must be set.")
        sys.exit(1)

def speech_recognize_once_from_file():
    """performs one-shot speech recognition with input from an audio file"""
    # <SpeechRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=inputfilename)
    # Creates a speech recognizer using a file as audio input, also specify the speech language
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, language="en-US", audio_config=audio_config)

    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    
    #creating dataframe and save the output into CSV format
    df = pd.DataFrame()  #pd.DataFrame(columns=['comment'])
    df['comment']=[str(result.text)] 
    #
    df.to_csv('C:/Swadesh/MMAI/MMAI 844/training/speech2text.csv')
    
    # </SpeechRecognitionWithFile>
    
    try:
        CONNECTION_STRING = AZURE_STORAGE_CONNECTION_STRING

    except KeyError:
        print("AZURE_STORAGE_CONNECTION_STRING must be set.")
        sys.exit(1)        
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

        # Instantiate a new ContainerClient
    container_client = blob_service_client.get_container_client(container_name)
      

    try:
        # Create new Container in the service
        container_client.create_container()

        # Instantiate a new BlobClient
        blob_client = container_client.get_blob_client(outputfilename)
        print("")
        print("")
        print ("Output file is uploaded to Blob storage")

        # [START upload_a_blob]
        # Upload content to block blob
        with open(outputfilename, "rb") as data:
            blob_client.upload_blob(data) #, blob_type="BlockBlob"
        # [END upload_a_blob]

        # [START delete_blob]
        #blob_client.delete_blob()
        # [END delete_blob]

    finally:
        # Delete the container
        #container_client.delete_container()
        pass

#speech_recognize_once_from_mic() 
speech_recognize_once_from_file()      