from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(H, W, feature_names, documents, no_top_words, no_top_documents):

    for topic_idx, topic in enumerate(H):

        topic_x = (" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

        topic_xs.append(topic_x)
        top_doc_indices = np.argsort( W[:,topic_idx] )[::-1][0:no_top_documents]

        for doc_index in top_doc_indices:
              topic_features.append(documents[doc_index])

    return topic_features, topic_xs


###########################################################################
#FLASK APP#################################################################
###########################################################################

app = Flask(__name__)

#full_topics = []
topic_xs = []
topic_features = []
no_topics = 2
no_top_words = 1
no_top_documents = 2

@app.route("/")
def index():
  return render_template("app-interface.html")

@app.route("/transfer", methods=["POST"])
def transfer():
  response = []
  response.clear()

  # Get message from Web-Interface
  message = request.get_json(force=True)
  print("Message: ", message)
  no_topics = int(message[0])
  no_top_words = int(message[1])
  no_top_documents = int(message[2])
  full_text = message[3]

  rock_list = [i[0] for i in full_text]
  print(rock_list)

  # Encode Emojis & Umlaute
  rock_list2 = []
  for l in rock_list:
    try:
      l = str(l)
      item = l.encode('utf8')
      rock_list2.append(item)
    except:
      print(l)

  print("Testing Point: a")
  documents = rock_list2
  print("Rock_List 2: ", rock_list2)

  # NMF is able to use tf-idf
  tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2)
  print("Testing Point: b")
  tfidf = tfidf_vectorizer.fit_transform(rock_list2)
  print("Testing Point: c")
  tfidf_feature_names = tfidf_vectorizer.get_feature_names()
  print("Testing Point: d")

  # Run NMF
  try:
    nmf_model = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)
    nmf_W = nmf_model.transform(tfidf)
    nmf_H = nmf_model.components_
    print("2")

    # Run Dimensionality reduction using Non-Negative Matrix Factorization
    display_topics(nmf_H, nmf_W, tfidf_feature_names, rock_list, no_top_words, no_top_documents)
  except:
    print("Oops!  Too little data for ML Model")
    topic_xs.append("Too little data!")
    topic_features.append("No output- Please adjust Category or ML Input parameters!")

  #Catching the response -> to JSON for FLASK request
  response = jsonify(topic_xs, topic_features)
  print(response)

  rock_list.clear()
  rock_list2.clear()
  topic_features.clear()
  topic_xs.clear()

  return response

if __name__ == '__main__':
 absl_app.run(main)
