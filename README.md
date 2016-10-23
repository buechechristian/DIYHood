# NeuroCritic

*NeuroCritic was fully developed during a 36-hour hackathon, mhacks8, on October 7-9 2016. It was built by Christian Bueche, Chris Withers, and Boston Walker.*
<br/>

<b>What it does:</b>
<br/>
Our neural network has been trained on a database of hundreds of independent art reviews, and will generate a unique critical response to any photo you upload.

<b>How we built it:</b>
<br/>
We adapted a classic LSTM recurrent neural network model to predict art reviews character-by-character using a dataset we scraped and cleaned from art bloggers. The neural net is seeded with feature data from Microsoft's Cognitive Services computer vision API, guaranteeing a unique and vaguely relevant critique with every user interaction!

<b>Challenges we ran into:</b>
<br/>
We weren't able to find a cloud platform that allowed us to install our API and dependency packages, so we had to quickly develop a locally hosted solution for a working demo. We also had to create our dataset completely from scratch

<b>Accomplishments that we're proud of & What we learned:</b>
<br/>
We are super proud to say we tackled all of the following: training a neural net (it was the first time for most of us), parsing complex json structures, creating a custom API, using google cloud services, and developing a cross-platform web app that interfaces with our API.

<b>What's next for NeuroCritic:</b>
<br/>
Our neural net is hungry! We plan on feeding it more web-scraped text from art-critical sources so it can continue to find its artistic voice.

<b>Built With:</b>
<br/>
python, 
google-cloud,
microsoft-computer-vision-api,
html5,
css3,
machine-learning

<b>How to Deploy</b>
<br/>
1. git clone <br/>
2. Create and enter virtual envrionment (source venv/bin/activate) <br/>
3. install dependencies from requirements.txt (pip install -r requirements.txt)  <br/>
4. Run api.py <br/>
5. Run app.py <br/>
6. Navigate to http://127.0.0.1:5000 <br/>
7. See what NeuroCritic has to say about your art! <br/>
