"'' ('Bismillahir Rahmanir Rahim') """
from textatistic import Textatistic
import textstat
import os
from xml.etree import ElementTree
from textblob import TextBlob

file_name = 'File2.xml'
full_file = os.path.abspath(os.path.join('Data', file_name))

dom = (ElementTree.parse(full_file))

review = dom.findall('review')

number_row_review_dataset = 0
for rvw in review:
    review_counter = rvw.find("review_text").text
    if not review_counter:
        number_row_review_dataset = 0
    else:
        number_row_review_dataset = number_row_review_dataset+1

number_readability_features = 6

linguistic_features_data_array = [[0 for array_column in range(number_readability_features)] for array_row in range(number_row_review_dataset)]

for rvw in review:
    review_text = rvw.find("review_text").text
    helpful = rvw.find("helpful").text

    # SUBJECTIVITY
    Review_Text_Blob = TextBlob(review_text)

    print(Review_Text_Blob.sentiment.subjectivity)