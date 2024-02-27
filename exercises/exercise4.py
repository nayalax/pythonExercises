# from colorama import Fore
import os

movieList = []
menu = {
    '1': 'Add a movie',
    '2': 'Delete a movie',
    '3': 'Show movie list',
    '4': 'Search',
    '5': 'Exit'
}

def main():
    while True:
        os.system("cls")
        menuOption = showMenu()
        if menuOption == '1':
            addMovie()
        elif menuOption == '2':
            deleteMovie()
        elif menuOption == '3':
            showMovieList()
        elif menuOption == '4':
            searchMovies()
        elif menuOption == '5':
            print("Exiting the movie directory app.")
            break
        else:
            print("Invalid option, please select 1 - 5")
            input("Press ENTER to continue...")
    
def showMenu():
    userInput = input("Movie Menu: \n" + str(menu).strip("{}") + "\n")
    return userInput

def addMovie():
    userInput = input("Movie title? \n").lower()
    if (userInput in movieList):
        print("Movie already exists, please add a new movie.\n" + str(movieList))
        input("Press ENTER to continue...")
    else:
        movieList.append(str(userInput))
        print(userInput + " has been added.")
        input("Press ENTER to continue...")
            
def deleteMovie():
    if (len(movieList) == 0):
        print("ATTN: There are no movies in the list to delete. Please add a movie to the list.")
        input("Press ENTER to continue...")
    else:
        userInput = input("Which movie do you want to delete? \n").lower()
        if (userInput not in movieList):
            print("Movie not found in list. \n")
            input("Press ENTER to continue...")
        else:
            movieList.remove(userInput)
            print(userInput + " has been removed.")
            input("Press ENTER to continue...")
        
def showMovieList():
    if (len(movieList) == 0):
        print("The movie list is empty.")
        input("Press ENTER to continue...")
    else: 
        print("Movies saved in list: \n")
        for movie in movieList:
            print(str(movie).upper() + "\n")
        input("Press ENTER to continue...")
        
def searchMovies():
    userInput = input("Search movie: \n").lower()
    if (movieList.count(userInput) > 0):
        index = movieList.index(userInput)
        print("Movie found! \n" + str(movieList[index]))
        input("Press ENTER to continue...")
    else:
        response = input("Movie not found. Would you like to add it to the list? (Y/n) \n").lower()
        if (response == 'y'):
            addMovie()
    
             
    
if __name__ == "__main__":
    main()
        
    


