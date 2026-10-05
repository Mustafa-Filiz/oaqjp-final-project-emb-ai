''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows emotion scores and 
        dominated emotion for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    label = response['label']
    score = response['score']
    # Return a formatted string with the emotions
    return f"For the given statement, the system response is 
    'anger': {response['anger']}, 'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 'joy': {response['joy']} and 
    'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)