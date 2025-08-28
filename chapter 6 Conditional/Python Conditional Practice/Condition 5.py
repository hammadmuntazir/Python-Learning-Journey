'''
Weather Activity Suggestion
problem:Suggest an activity based on the weather (e.g.Sunny-Go for a walk,Rainy-Read a  book,Snowy-Build a snow man
'''
Weather={

    "Sunny":"Go for a walk",
    "Rainy":"Read a book",
    "Snowy":"Build a snowman"
}
weather=input("Enter condition of weather")
print(Weather[weather])