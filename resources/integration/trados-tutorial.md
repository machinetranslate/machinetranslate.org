---
nav_order: 3
grand_parent: Resources
parent: Connecting engines to translation software
title: How to get machine translation in Trados
description: Setting up machine translation plugins in Trados
---


**Trados** is a translation management system with **machine translation plugins** for many machine translation providers.

A Trados machine translation plugin requires an API key.  

The documentation and screen captures are based on Trados Studio 2021™.

## Amazon Translate (AWS)


### How to obtain an API key


Read [here](/api-keys#amazon-translate-aws) for more details.  


### How to set up the Trados plugin for Amazon Translate (AWS)


1. Open your desktop version of Trados.

2. Go to **Add-ins > RWS AppStore**. Search for **Amazon Translate MT Provider** and download it. Restart Trados.


3.  Go to **Project Settings**. In the **Translation Memory and Automated Translation** settings window select the provider by clicking **Use...** > **Amazon Translate Trados Plugin**.



![How to set up the Trados plugin for Amazon Translate (AWS)pic1](/trados-images/trados_for_amazon1.png)


![How to set up the Trados plugin for Amazon Translate (AWS)pic2](/trados-images/trados_for_amazon2.png)  


1.  Enter necessary credentials in the **Authentication** window.


    4.1  Select **Access key  / Secret access key** in the **Choose AWS auth type** drop-down menu.

    4.2 Enter the **AWS region name**, **Access key**, and **Secret access key** credentials in the appropriate fields. Check the **Save access keys for future sessions** option.

    4.2 Confirm by clicking **OK**.

![How to set up the Trados plugin for Amazon Translate (AWS)pic3](/trados-images/trados_for_amazon3.png)  


The **Amazon Translate Trados Plugin** plugin is now visible in the **Translation Memory and Automated Translation** settings window. You may start using this service now.


## DeepL


### How to obtain an API key


Read [here](/api-keys#deepl) for more details.  


### How to set up the Trados plugin for DeepL


1.  Open your desktop version of Trados.


2.  Go to **Add-ins > RWS AppStore**. Search for **DeepL Translation Provider** and download it. Restart Trados.


3.  Go to **Project Settings**. In the **Translation Memory and Automated Translation** settings window select the provider by clicking **Use...** > **DeepL MT Translation Provider**.


![How to set up the Trados plugin for Deeplpic1](/trados-images/trados_for_deepl1.png)  


4.  Enter the API key. Click **OK**.


5.  Add the following domains to your firewall/antivirus exceptions: www2.deepl.com and www.api.deepl.com.


6.  Please check if the API key is added correctly. Read this article for more information: [https://gateway.sdl.com/apex/communityknowledge?articleName=000013232](https://gateway.sdl.com/apex/communityknowledge?articleName=000013232)


The **DeepL MT Translation Provider** plugin is now visible in the **Translation Memory and Automated Translation** settings window. You may start using this service now.


## ModernMT


### How to obtain an API key  


Read [here](/api-keys#modernmt) for more details.  


### How to set up the Trados plugin for ModernMT


1.  Open your desktop version of Trados.


2.  Go to **Add-ins > RWS AppStore**. Search for **ModernMT** and download it. Restart Trados.


3.  Go to **Project Settings**. In the **Translation Memory and Automated Translation** settings window select the provider by clicking **Use...** > **Modern MT Adaptive Neural Machine Translation**.



![How to set up the Trados plugin for ModernMTpic1](/trados-images/trados_for_modernmt1.png)



4. Enter the API key. Click **OK**.


![How to set up the Trados plugin for ModernMTpic2](/trados-images/trados_for_modernmt2.png)


5.  You may select one or more translation memories to use with your project. Check the **Use** check box for each translation memory you wish to use. If you check the **Update** check box of a translation memory, it will learn from the corrections you make in a given translation. You may select this check box for only one translation memory.

![How to set up the Trados plugin for ModernMTpic3](/trados-images/trados_for_modernmt3.png)


The **Modern MT Adaptive Neural Machine Translation** plugin is now visible in the **Translation Memory and Automated Translation** settings window. You may start using this service now.


## Google Cloud Translation Basic (or Google Translate API v2)  


### How to obtain an API key


Read [here](/api-keys#google-cloud-translation-basic-or-google-translate-api-v2) for more details.  


### How to set up the Trados plugin for Google Cloud Translation Basic (or Google Translate API v2)


1.  Open your desktop version of Trados.


2.  Go to **Add-ins > RWS AppStore**. Search for **MT Enhanced Plugin for Trados Studio** and download it.


![How to set up the Trados plugin for Google Translation Basicpic1](/trados-images/trados_for_google1.png)


3.  Restart Trados.


4.  Go to **Project Settings**. In the **Translation Memory and Automated Translation** settings window select the provider by clicking **Use...** > **MT Enhanced Trados Plugin**.



![How to set up the Trados plugin for Google Translation Basicpic2](/trados-images/trados_for_google2.png)



5.  Open the uppermost drop-down menu to choose which MT provider you want to use. Select **Google Translator**.


6.  Below the uppermost drop-down menu, there is another one in which you can select which version of the Google Translate API you wish to use. Open it and select **V2-Basic Translation**.


7.  Enter the API key in the field below. Check the **Save Google key**.


8.  Click **OK**.


![How to set up the Trados plugin for Google Translation Basicpic3](/trados-images/trados_for_google3.png)


The **MT Enhanced Plugin for Trados Studio** plugin is now visible in the **Translation Memory and Automated Translation** settings window. It is displayed as **MT Enhanced using Google Translate Basics** in the opened window. You may start using this service now.



### How to set up the Google API Validator plugin for Trados (optional)


This plugin is not required for the **Google Cloud Translation Basic (or Google Translate API v2)** service to work with Trados, but it enhances the usability of this MT. The plugin has been developed to provide a simple and fast way to validate the credentials being used to access the Google Translate API.


![How to set up the Trados plugin for Google Translation Basicpic4](/trados-images/trados_for_google4.png)


1.  Open your desktop version of Trados.


2.  Go to **Add-ins > RWS AppStore**. Search for **Google API Validator** and download it. By default, it is saved in the following destination: C:\Users\User1\AppData\Roaming\SDL Community\AppStore Integration\Downloads\GoogleApiValidator.Setup.zip.

In your system, the \Users\User1 part of the path shown here will most likely be different. The path has been included here as an example, not a precise indication of the .zip file location.


1.  Install the file by clicking it and following the on-screen commands.



2.  After the plugin is installed, restart Trados. The plugin is now ready for use.



 More information on this plugin is available **[here](https://community.sdl.com/product-groups/translationproductivity/w/customer-experience/5493/google-api-validator).**
