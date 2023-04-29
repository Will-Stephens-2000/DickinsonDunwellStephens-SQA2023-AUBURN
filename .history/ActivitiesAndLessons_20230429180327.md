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
    
    