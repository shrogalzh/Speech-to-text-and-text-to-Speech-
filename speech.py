#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install ibm_watson


# In[4]:


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[5]:


apikey = 'Demh2ZcmA0aQpbF8lSzOdocP4AScVLHIUatCJFJQfn40'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/939241d1-2cac-4f94-9ec9-e62f4724192e'


# In[6]:


authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


# In[8]:


with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hi Shrog!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)


# In[ ]:




