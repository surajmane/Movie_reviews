from reviews_import import *

"""Get the movie about info and the average movie ratings from Rottentomatoes given the movie name

Args:
    url(str) = The name of the movie you'd like the review of

returns: A small about info of the movie and the average rating from Rottentomatoes

"""

def webscraper():
    
    movie_name = sys.argv[1]
    url = "https://www.rottentomatoes.com" + "/m/" + movie_name
    print(url)
    with urllib.request.urlopen(url) as response: html = response.read()
    soup = BeautifulSoup(html, features='html.parser')
    # text = soup.get_text()
    # print(text)
    tags = soup.find(id="score-details-json")
    val = str(tags.contents)
    print('What the movie is about')
    print(soup.find("meta", {"name":"description"})['content'])
    # soup_val = BeautifulSoup(val, features='html.parser')
    val_tknz = word_tokenize(val)
    #print(val_tknz)
    rating = val_tknz.index('averageRating')
    rating_index = rating+4
    print(val_tknz[rating], "=", val_tknz[rating_index])
    
 
 
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Word Frequency generator')

    parser.add_argument('URL', type=str,
        help='The URL to fetch the word densities from')
    args = parser.parse_args()
    info = webscraper()