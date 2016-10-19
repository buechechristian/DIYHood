# NeuroCritic

<b>What it does</b>
Our neural network has been trained on a database of hundreds of independent art reviews, and will generate a unique critical response to any photo you upload.

How we built it
We adapted a classic LSTM recurrent neural network model to predict art reviews character-by-character using a dataset we scraped and cleaned from art bloggers. The neural net is seeded with feature data from Microsoft's Cognitive Services computer vision API, guaranteeing a unique and vaguely relevant critique with every user interaction!

Challenges we ran into
We weren't able to find a cloud platform that allowed us to install our API and dependency packages, so we had to quickly develop a locally hosted solution for a working demo. We also had to create our dataset completely from scratch

Accomplishments that we're proud of & What we learned
We are super proud to say we tackled all of the following: how to train a neural net (it was the first time for most of us), parse complex json structures, create a custom API, use google cloud services, develop a cross-platform web app that interfaces with our API.

What's next for NeuroCritic
Our neural net is hungry! We plan on feeding it more web-scraped text from art-critical sources so it can continue to find its artistic voice.

Built With
python
google-cloud
microsoft-computer-vision-api
html5
css3
machine-learning
