
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import time
import os
from nltk.parse import stanford
from nltk.tag.stanford import StanfordPOSTagger
os.environ['STANFORD_PARSER'] = './stanford-parser-full-2017-06-09/'
os.environ['STANFORD_MODELS'] = './stanford-parser-full-2017-06-09/'

parser = stanford.StanfordParser(model_path="./stanford-parser-full-2017-06-09/englishPCFG.ser.gz")
st = StanfordPOSTagger(model_filename='./stanford-parser-full-2017-06-09/english-left3words-distsim.tagger',path_to_jar='./stanford-parser-full-2017-06-09/stanford-postagger.jar')
speech_to_text = SpeechToTextV1(
    username='e2502766-0bbd-4244-a087-4afa13ed5e1f',
    password='nVhFCCpLOH6u',
    x_watson_learning_opt_out=False
)
week = ( '월', '화', '수', '목', '금', '토', '일' )

with open(join(dirname(__file__), './transcript.mp3'),'rb') as audio_file:
    result = (json.dumps(speech_to_text.recognize(audio_file, content_type='audio/mp3', timestamps=True,
        word_confidence=True),indent=2))
    r = json.loads(result)
    #print ( r['results'][0]['alternatives'][0]['transcript'])
    parsinglist = st.tag(r['results'][0]['alternatives'][0]['transcript'].split())
    print(parsinglistsopd)
    now = time.localtime()
    for data in parsinglist:
        if data[1] =='NN' and data[0].lower() =='tomorrow':
            print(data[0].lower()+' is : %s' % (week[(now.tm_wday + 1) % 7]))
        if data[1] == 'NN' and data[0].lower() == 'yesterday':
            print(data[0].lower()+' is : %s' % (week[(now.tm_wday - 1) % 7]))

