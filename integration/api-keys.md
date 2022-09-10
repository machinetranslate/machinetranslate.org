# How to get API keys for machine translation engines

A machine translation API key is required to integrate machine translation into other applications and systems, either as a developer or as an user, for example:
- To integrate a machine translation API into systems and applications.
- To use machine translation in a translation application, like a TMS or CAT tool.


## Amazon Translate (AWS)  


Create an **[AWS account](https://aws.amazon.com/)**
![How to obtain an API key for Amazon Translate AWSpic1](api-images/amazon4.png)  

1. You need your debit/credit card to accomplish this step. One USD/EUR is then temporarily charged to your bank account. Provide your personal details. In the next step select the payment plan:  

![How to obtain an API key for Amazon Translate AWSpic2](api-images/amazon5.png)  

2. Next, configure your account locally. Download and install the **[AWS CLI](https://aws.amazon.com/cli/)** (Command Line Interface). Additional information on how to accomplish this task may be found in the **[AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html)**.  

![How to obtain an API key for Amazon Translate AWSpic3](api-images/amazon6.png)  

3. Look for necessary credentials in your **AWS Management Console**.  
 
4. Click the name of your account in the upper, right corner of the page.  

5. Select **My Security Credentials**.  

6. Click **Access keys (access key ID and secret access key)**.  
 
7. Generate the key. Download the key file. Remember to store it in a safe place.  
 
8. Run AWS CL by **[opening a windows command prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089).** Type in `aws configure`.  
 
9. When prompted enter the required data. Confirm by pressing Enter after each line. When prompted for the **Default region name** enter `us-west-2` or follow the instructions given here: [https://docs.aws.amazon.com/general/latest/gr/rande.html](https://docs.aws.amazon.com/general/latest/gr/rande.html).  

10. Type in `aws configure` again. This is an example of what you should see then:  

![How to obtain an API key for Amazon Translate AWSpic4](api-images/amazon7.png)  

You have successfully set up your AWS credentials, incl. your API key.  


## 4.2 DeepL  


Create a DeepL account [here](https://www.deepl.com/pro.html)  


1. Select DeepL Pro payment plan. You need your debit/credit card to register your account. Provide your personal details. Confirm each step.  

 
2. Press **Retrieve your Authentication Key** on the last screen. 


3. Go to **Account**. Your API key is at the bottom of the screen under ** Authentication Key for DeepL API**. Copy it and store it in a safe location.  


## 4.3 ModernMT  


Create a ModernMT account [here](https://www.modernmt.com/pricing/).  

1. Click **Plugins for translators** > **Get a license**.  


2. You need your debit/credit card to register your account. Provide your personal details.  


3. Click **Start your plan**.  


4. Copy your activation key from the **Here’s your activation key** field. Store it in a safe location.  


## Google Cloud Translation Basic (or Google Translate API v2)  


To use this MT vendor you need to have your regular Google Account. Set it up and log in to it. Then log in [here](https://console.developers.google.com/cloud-resource-manager).

1. Go to **Billing** > **Add a billing account**. Accomplish all the required steps of the procedure.  
 
![How to obtain an API key_Google_pic1](api-images/google5.png)  

2. You should find yourself in the **Dashboard** view. As there are frequent changes to the **Google Cloud Platform** the page you find yourself may be different.  

![How to obtain an API key_Google_pic2](api-images/google6.png)  

3. Type in `new project` in the search window. Click **Create a Project IAM & Admin**.  
 
![How to obtain an API key_Google_pic3](api-images/google7.png)  

4. Assign a name to your project in the **Project name** field (for example **CATpluginproject**). Write it down for future use. Click **Create**.  

![How to obtain an API key_Google_pic4](api-images/google8.png)  

5. Type in your project name in the search window and press **Enter**. Click the project name in the results window.  

6. In the upper, left corner of the page, the drop-down menu has changed its name to the name of your project. Open the menu, and click the name of this project (for example **CATpluginproject**).  

 ![How to obtain an API key_Google_pic5](api-images/google9.png)  

7. The name of your project is now visible in the **Search** window in the middle of the upper part of the page. Click **Menu** (three horizontal lines one under another in the left corner) > **APIs & services**.  

 ![How to obtain an API key_Google_pic6](api-images/google10.png)

8. Click **ENABLE APIS AND SERVICES**.  
 
![How to obtain an API key_Google_pic7](api-images/google11.png)

9. In the left margin click **Machine Learning**.  
 
![How to obtain an API key_Google_pic8](api-images/google12.png)

10. Click **Cloud Translation API** > **Enable**.  
 
![How to obtain an API key_Google_pic9](api-images/google13.png)  
![How to obtain an API key_Google_pic10](api-images/google14.png)  

11. To use this API, you need credentials. Click **Create credentials** to get started.  
 
![How to obtain an API key_Google_pic11](api-images/google15.png)

12. From the **Select an API** drop-down menu select **Cloud Translation API**.  
 
![How to obtain an API key_Google_pic12](api-images/google16.png)  

13. Click **Cancel**.  
 
![How to obtain an API key_Google_pic13](api-images/google17.png)  

14. In the upper part of the dashboard, click **CREATE CREDENTIALS** > **API key**.  
 
![How to obtain an API key_Google_pic14](api-images/google18.png)  
![How to obtain an API key_Google_pic15](api-images/google19.png)  

15. Wait for the API key to be created. Remember to copy it and store it in a safe location. Click **RESTRICT KEY** to prevent unauthorized use in production.  
 
![How to obtain an API key_Google_pic16](api-images/google20.png)   

16. Allow the **Restrict key** option. In the drop-down menu select **Cloud Translation API**. Click **Save**.  
  
![How to obtain an API key_Google_pic17](api-images/google21.png)  


You now have your API key set up.  
