import requests
from imdb import Cinemagoer
import streamlit as sl

sl.write("> Welcome! To isg32's Vidsrc Worker")
def xlol():
    sl.write("# Search Movies Here")
    movie = sl.text_input("Enter the movie name:")
    search_button = sl.button("Search")

    if search_button and movie or movie:
        ia = Cinemagoer()
        results = ia.search_movie(movie)
        #sl.write(results)

        if results:
            for i in range(len(results)):
                mv = results[i]  # First result
                URL = ia.get_imdbURL(mv)  # URL for first result
                imdurl = URL
                vidsrcurl = "https://vidsrc.xyz/embed/movie/"
                vidurlf = imdurl.replace("https://www.imdb.com/title/", "https://vidsrc.xyz/embed/movie/")
                x = vidurlf
                sl.success(f"""
                            # ![]({results[i]['cover url']})\n\n
                            *Title:*  
                            {results[i]['title']}\n
                            _Streaming Link:_  [Play]({x})""")
        else:
            sl.warning("No results found for the given movie name.")

def ylol():
    sl.write("# Search TV Here")
    movie = sl.text_input("Enter the Tv Series name:")
    search_button = sl.button("Search")

    if search_button and movie or movie:
        ia = Cinemagoer()
        results = ia.search_movie(movie)
        #sl.write(results)

        if results:
            for i in range(len(results)):
                sv = results[i]  # First result
                URL = ia.get_imdbURL(sv)  # URL for first result
                imdurl = URL
                vidsrcurl = "https://vidsrc.xyz/embed/tv/"
                vidurlf = imdurl.replace("https://www.imdb.com/title/", "https://vidsrc.xyz/embed/tv/")
                x = vidurlf
                sl.success(f"""
                            # ![]({results[i]['cover url']})\n\n
                            *Title:*  
                            {results[i]['title']}\n
                            _Streaming Link:_  [Play]({x})""")
        else:
            sl.warning("No results found for the given movie name.")

def zlol():
    sl.write("""
    # Isg32's Vidsrc (Api implemetation)
    
    ---
    > What is this?
            
        This program is a Streamlit web application that allows users to search for movies and TV series and obtain streaming links from the VidSrc platform. It consists of three main functionalities:
        
        Movie Search (xlol function):
        
        Users can enter the name of a movie, click the "Search" button, and the program will fetch search results from IMDb using the IMDbPY library.
        If results are found, it displays the cover image, title, and a streaming link for each result.
        TV Series Search (ylol function):
        
        Similar to the movie search, users can enter the name of a TV series, click the "Search" button, and the program will fetch search results from IMDb.
        It displays the cover image, title, and a streaming link for each result.
        About Section (zlol function):
        
        This section provides information about the application, presented with a Streamlit markdown.
        Main Function (main function):
        
        The main function sets up the Streamlit sidebar with three tabs: "Movies," "Series," and "About."
        Depending on the selected tab, it calls the corresponding function (xlol, ylol, or zlol) to display the content.
        Additional (commented-out) Code:
        
        There is commented-out code that seems to be related to fetching and displaying the latest released episodes from VidSrc. This functionality is currently disabled.
        Execution:
        
        When the script is executed, the Streamlit web application is launched.
        Users can interact with the sidebar to choose between searching for movies, TV series, or accessing information about the application.
        
    © Copyright 2022 [Sapan Gajjar](https://github.com/isg32). All rights reserved
    """)


def main():
    sl.sidebar.title("SEARCH METHOD")
    tabs = ["Movies", "Series", "About"]
    selected_tab = sl.sidebar.radio("Select Method", tabs)

    if selected_tab == "Movies":
        xlol()
    elif selected_tab == "Series":
        ylol()
    elif selected_tab == "About":
        zlol()

if __name__ == "__main__":
    main()


#
# api_url = 'https://vidsrc.xyz/episodes/latest/page-1.json'
# response = requests.get(api_url)
# cachedBody = []
# json_data = response.json()

# for i in range(len(json_data["result"])):
#     cachedBody.append(json_data["result"][i])
#
# markdown_code = ""

# for item in cachedBody:
#     markdown_code += f"""
# | {item["show_title"]} | {item["season"]} | {item["episode"]} | [Play]({item["embed_url"]}) |
# |----------------------|------------------|-------------------|-----------------------------|
# """
#
# sl.title("VidSrc: Display")
# sl.write("> Latest Released Episodes Here!")
# sl.write(f"""
# | Name | Season | Episode | URL|
# |------|--------|---------|----|
# {markdown_code}
# """)

