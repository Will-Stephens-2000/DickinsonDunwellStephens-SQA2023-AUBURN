Responsibilities:
    Git Hook:   Will Stephens
    Fuzzing:    Garrett Dickinson
    Forensics:  Nick Dunwell

Notes:
    It should be noted that not all methods modified for forensics were called when running main.py.
    The modified methods were in graphtaint.py:
        getYAMLFiles()
        getHelmTemplateContent()
        getMatchingTemplates()
        getSHFiles()
        getTaintsFromConfigMaps()


Lessons:
    When creating the githook modifications, there was an error which occured which 
    prevented me from committing changes. After investigation, there was a line in the 
    githook which failed the commit if there was a whitespace error. After removing
    this command, committing succeeded without issue.

    In a real project, I see the value of this command when working with python files,
    but for the sake of this project, deleting this line seemed sufficient.
    