# DS
ML for stalkering social networks

* tweets_extraction.ipynb - parsing tweets using Twitter API

* input.py & fromfile.py scraping vk groups, the first reads domens from command line

*  networking_for_introverts.py - parsing geolocated photos from vk anf instagram (may be useful in case you want to find profiles in social networks of someone you met at an event)

* clean.py - preprocessing text data from vk for k-means

* prepare_text.ipynb - tokenization, lemmatization, removing stop words, vectirization (tf-idf) for [BigARTM](http://bigartm.org)

* topic_modeling.ipynb - extracting topics using ML model ARTM

* k-means.ipynb - text clastering for comparison

* vw_classifier.ipynb - segmentation of auditory using [VowpalWabbit](https://github.com/VowpalWabbit/vowpal_wabbit) Classifier
based on stochastic gradient descent and hyperopt with python [wrapper](https://pypi.org/project/vowpalwabbit) for VW lib
