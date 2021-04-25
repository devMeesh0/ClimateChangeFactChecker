# Climate Change Fact Checker

### This is a web app that displays a sorted list of different types of fake news
How it works:
1. We use a webscrapper along with a two layers of filters </br>
  a. First layer filter uses NLP model to determine if a tweet contains fake news
  b. Second layer filter sorts into category by checking for keywords
2. Tweet is added to database along with its category
3. Web app fetches tweets from data and they are displayed on our webapp

Technologies Used: <br/>
<img src="https://www.tensorflow.org/images/tf_logo_social.png" alt="tensorflow" width="100"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" alt="python" width="100"/>
<img src="https://download.logo.wine/logo/MySQL/MySQL-Logo.wine.png" alt="mySQL" width="150"/>
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--K2q0A5SX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/2elgd5zp07wkeilkna63.png" alt="heroku" width="150"/>
<img src="https://miro.medium.com/max/800/1*Q5EUk28Xc3iCDoMSkrd1_w.png" alt="flask" width="150"/>
