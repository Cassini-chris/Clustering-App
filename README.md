# Clustering-App
### Topic-Modeling aka. unsupervised learning using Non-negative matrix factorization

Please checkout:

## [>>> Final Application](https://ml-clustering.ew.r.appspot.com// "Clustering APP")


![Clustering_Pic](https://github.com/cassini-chris/Clustering-App/blob/main/_GITHUB/readme/images/Clustering_app2.JPG?raw=true)

In detail, in this project I have explored topic modeling via Non-negative matrix factorization. The Clustering APP is an application that identifies Clusters by running topic modeling over an uploaded CSV file. The application is powered by GAE and runs on Python 3.9. Although topic modeling is not new, the idea of this project is to highight Cloud technologies, predominately GCP services to make clustering tangible and accessible for everyone. In detail, to build and run the application, I only used:
- [x] Google App Engine
- [x] Flask


__Tl;dr__: Machine Learning does not have to be a black-box. Applications that use ML generally consist of different building blocks. My motivation to build, deploy and open-source applications is entirely focused on educational purposes. Further, I want to introduce a simple guide on how to leverage ML applications in the Cloud and make them accessible to the wider public. In this repo you find entire code for performing Clustering over a CSV file.

the repo does hold the following:
- [x] app.yaml (to specify the python runtime)
- [x] cron.yaml (to avoid shutting down of the Google app engine instance)
- [x] main.py (the python application with the NMF model)
- [x] requiremenrs.txt (to specify the dependencies)
- [x] A static folder (that holds the css, images, and favicons used)
- [X] A template folder (that holds the app interface)
- [X] A dummy_data folder (that holds a CSV example file)


