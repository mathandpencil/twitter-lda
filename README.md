##### Download From Twitter Archive

##### Parse the content

cat tweets.csv | awk -F"," '{print $6}' > tweets_content.dat

##### Parse HTML

python parse_twitter_csv.py tweets_content.dat > twitter_urls.dat

#### Get the real-HTML with diffbot

python get_html_with_diffbot.py twitter_urls.dat

#### Download results from diffbot API

curl http://api.diffbot.com/v3/bulk/download/asdfasdfasdfasdf-MISITI_data.json -o results.json

#### Make the corpus


##### Run LDA

python lda.py -f corpus.txt -k 10 --alpha=0.5 --beta=0.5 -i 25