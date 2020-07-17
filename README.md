Step1
In the Azure Portal, create resource group

Step2
Click on “Create Resource” then search “Speech”, create the resource using free price tier under the same resource group created in the preious step.

Step3
Wait until it says "Your deployment is complete", then click "Go to resource"

Step4
Copy the Key, region from the "Key and Endpoint" section. Copy it into a notepad for following steps.

Step5
Click on “Create Resource” then search click “Text Analytics” and create the resource using free price tier under the same resource group created in the preious step.

Step6
Wait until it says "Your deployment is complete", then click "Go to resource"

Step7
Copy the Key and EndPoint from the "Key and Endpoint" section. Copy it into a notepad for following steps.

Step8
Click on “Create Resource” then select “Web App”, create the resource using free price tier under the same resource group created in the preious step.

Step9
Wait until it says "Your deployment is complete", then click "Go to resource"

Step10
Stepup GitHub Repository and Sync it with Local folder on your computer.

Step 11
Copy index_from_microphone.html, microsoft.cognitiveservices.speech.sdk.bundle.js, token.php from https://github.com/BroadviewQueens/Speech2Text to the local folder used in the previous step

Step 12
Open GitHub Desktop and commit the changes, push the local commit by clicking "Push origin"

Step 13
Go to Azure Portal, open the Web App created, and click on Deployment Center

Step 14
Select GitHub repository and select build "Kudu", click next and complete the setup

Step 15
Click on "Configuration" under "Settings" in the left pane.

Step 16
Click on "Default Documents", and then click "New Document" and add "index_from_microphone.html" and save.

Step 17
Browse the WebApp and test the Speech-to-text and Text Analytics functionality.
