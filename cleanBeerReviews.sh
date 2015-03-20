#capture output
python scrapeBeerReviews.py | tee prep1.txt
# add the words "BEGIN NOW" to the beginning of each line
cat prep1.txt | sed 's/^/BEGIN NOW /' > prep2.txt
# add the word "END" to the end of each line
cat prep2.txt | sed 's/$/ END/' > beerReviews.txt