## 4. How to obtain API keys for MT plugins
### 4.1 Amazon Translate (AWS)
Create an **[AWS account](https://aws.amazon.com/)**
![How to obtain an API key for Amazon Translate AWSpic1](./images/trados/trados_AWS/2021-10-11_21_18_57-1.png)

 -  You need your debit/credit card to accomplish this step. One USD/EUR is then temporarily charged to your bank account. Provide your personal details. In the next step select the payment plan:


![How to obtain an API key for Amazon Translate AWSpic2](./images/trados/trados_AWS/2021-10-11_21_26_40-2.png)  


 - Next, configure your account locally. Download and install the **[AWS CLI](https://aws.amazon.com/cli/)** (Command Line Interface). Additional information on how to accomplish this task may be found in the **[AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html)**.

![How to obtain an API key for Amazon Translate AWSpic3](./images/trados/trados_AWS/2021-10-11_21_36_42-3.png)

 - Look for necessary credentials in your **AWS Management Console**.
 
 - Click the name of your account in the upper, right corner of the page.
 
 - Select **My Security Credentials**.
 
 - Click **Access keys (access key ID and secret access key)**.
 
 - Generate the key. Download the key file. Remember to store it in a safe place.
 
 -  Run AWS CL by **[opening a windows command prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089).** Type in `aws configure`.
 
 - When prompted enter the required data. Confirm by pressing Enter after each line. When prompted for the **Default region name** enter `us-west-2` or follow the instructions given here: [https://docs.aws.amazon.com/general/latest/gr/rande.html](https://docs.aws.amazon.com/general/latest/gr/rande.html).

  - Type in `aws configure` again. This is an example of what you should see then:

![How to obtain an API key for Amazon Translate AWSpic4](./images/trados/trados_AWS/2021-10-11_21_30_36-4.png)

You have successfully set up your AWS credentials, incl. your API key.

### 4.2 DeepL
Create a DeepL account [here](https://www.deepl.com/pro.html)

 -  Select DeepL Pro payment plan. You need your debit/credit card to register your account. Provide your personal details. Confirm each step.
 
 - Press **Retrieve your Authentication Key** on the last screen. 
 
 - Go to **Account**. Your API key is at the bottom of the screen under ** Authentication Key for DeepL API**. Copy it and store it in a safe location.

### 4.3 ModernMT
Create a ModernMT account [here](https://www.modernmt.com/pricing/).

- Click **Plugins for translators** > **Get a license**.

- You need your debit/credit card to register your account. Provide your personal details.

- Click **Start your plan**.

- Copy your activation key from the **Here’s your activation key** field. Store it in a safe location.

### 4.4 Google Cloud Translation Basic (or Google Translate API v2)
To use this MT vendor you need to have your regular Google Account. Set it up and log in to it. Then log in [here](https://console.developers.google.com/cloud-resource-manager).

 - Go to **Billing** > **Add a billing account**. Accomplish all the required steps of the procedure.
 
![How to obtain an API key_Google_pic1](./images/trados/trados_Google/2021-10-11_21_42_47-1.png)

 - You should find yourself in the **Dashboard** view. As there are frequent changes to the **Google Cloud Platform** the page you find yourself may be different.
 
![How to obtain an API key_Google_pic2](./images/trados/trados_Google/2021-10-11_21_44_52-2.png)

 - Type in `new project` in the search window. Click **Create a Project IAM & Admin**.
 
![How to obtain an API key_Google_pic3](./images/trados/trados_Google/2021-10-11_21_47_00-3.png)

 - Assign a name to your project in the **Project name** field (for example **CATpluginproject**). Write it down for future use. Click **Create**.

![How to obtain an API key_Google_pic4](./images/trados/trados_Google/2021-10-11_21_48_01-4.png)

 - Type in your project name in the search window and press **Enter**. Click the project name in the results window.
 
 - In the upper, left corner of the page, the drop-down menu has changed its name to the name of your project. Open the menu, and click the name of this project (for example **CATpluginproject**).
 
![How to obtain an API key_Google_pic5](./images/trados/trados_Google/2021-10-11_21_49_15-5.png)

 - The name of your project is now visible in the **Search** window in the middle of the upper part of the page. Click **Menu** (three horizontal lines one under another in the left corner) > **APIs & services**.
 
![How to obtain an API key_Google_pic6](./images/trados/trados_Google/2021-10-11_21_51_54-6.png)

 - Click **ENABLE APIS AND SERVICES**.
 
![How to obtain an API key_Google_pic7](./images/trados/trados_Google/2021-10-11_21_57_20-7.png)

 - In the left margin click **Machine Learning**.
 
![How to obtain an API key_Google_pic8](./images/trados/trados_Google/2021-10-11_21_58_36-8.png)

 - Click **Cloud Translation API** > **Enable**.
 
![How to obtain an API key_Google_pic9](./images/trados/trados_Google/2021-10-11_22_00_29-9.png)
![How to obtain an API key_Google_pic10](./images/trados/trados_Google/2021-10-11_22_01_51-10.png)

 - To use this API, you need credentials. Click **Create credentials** to get started.
 
![How to obtain an API key_Google_pic11](./images/trados/trados_Google/2021-10-11_22_02_39-11.png)

 - From the **Select an API** drop-down menu select **Cloud Translation API**.
 
![How to obtain an API key_Google_pic12](./images/trados/trados_Google/2021-10-11_22_04_11-12.png)

 - Click **Cancel**.
 
![How to obtain an API key_Google_pic13](./images/trados/trados_Google/2021-10-11_22_05_31-13.png)

 - In the upper part of the dashboard, click **CREATE CREDENTIALS** > **API key**.
 
![How to obtain an API key_Google_pic14](./images/trados/trados_Google/2021-10-11_22_06_55-14.png)
![How to obtain an API key_Google_pic15](./images/trados/trados_Google/2021-10-11_22_08_15-15.png)

 - Wait for the API key to be created. Remember to copy it and store it in a safe location. Click **RESTRICT KEY** to prevent unauthorized use in production.
 
![How to obtain an API key_Google_pic16](./images/trados/trados_Google/2021-10-11_22_09_21-16.png)

 - Allow the **Restrict key** option. In the drop-down menu select **Cloud Translation API**. Click **Save**.
  
![How to obtain an API key_Google_pic17](./images/trados/trados_Google/2021-10-11_22_11_03-17.png)

You now have your API key set up.
