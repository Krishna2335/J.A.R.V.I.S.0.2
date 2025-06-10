


def get_extension(text):

    if "python file" in text:
        ex = ".py"
    elif "java file" in text:
        ex = ".java"
    elif "text file" in text:
        ex = ".txt"
    elif "html file" in text:
        ex = ".html"
    elif "css file" in text:
        ex = ".css"
    elif "javascript file" in text:
        ex = ".js"
    elif "json file" in text:
        ex = ".json"
    elif "xml file" in text:
        ex = ".xml"
    elif "csv file" in text:
        ex = ".csv"
    elif "excel file" in text:
        ex = ".xlsx"
    elif "word file" in text:
        ex = ".docx"
    elif "pdf file" in text:
        ex = ".pdf"
    elif "image file" in text:
        ex = ".jpg"
    elif "audio file" in text:
        ex = ".mp3"
    elif "video file" in text:
        ex = ".mp4"
    elif "c file" in text:
        ex = ".c"
    elif "cpp file" in text:
        ex = ".cpp"
    elif "ruby file" in text:
        ex = ".rb"
    elif "php file" in text:
        ex = ".php"
    elif "shell script" in text:
        ex = ".sh"
    elif "markdown file" in text:
        ex = ".md"
    else:
        ex = ""
    return ex

def update_text(text):

    if "python file" in text:
        text = text.replace("python file", "")
        
    elif "java file" in text:
        text = text.replace("java file", "")
       
    elif "text file" in text:
        text = text.replace("text file", "")
      
    elif "html file" in text:
        text = text.replace("html file", "")
    
    elif "css file" in text:
        text = text.replace("css file", "")
       
    elif "javascript file" in text:
        text = text.replace("javascript file", "")
      
    elif "json file" in text:
        text = text.replace("json file", "")
       
    elif "xml file" in text:
        text = text.replace("xml file", "")
       
    elif "csv file" in text:
        text = text.replace("csv file", "")
        
    elif "excel file" in text:
        text = text.replace("excel file", "")
       
    elif "word file" in text:
        text = text.replace("word file", "")
        
    elif "pdf file" in text:
        text = text.replace("pdf file", "")
      
    elif "image file" in text:
        text = text.replace("image file", "")
      
    elif "audio file" in text:
        text = text.replace("audio file", "")
      
    elif "video file" in text:
        text = text.replace("video file", "")
     
    elif "c file" in text:
        text = text.replace("c file", "")
        
    elif "cpp file" in text:
        text = text.replace("cpp file", "")
      
    elif "ruby file" in text:
        text = text.replace("ruby file", "")
        
    elif "php file" in text:
        text = text.replace("php file", "")
        
    elif "shell script" in text:
        text = text.replace("shell script", "")
        
    elif "markdown file" in text:
        text = text.replace("markdown file", "")
        
    else:
        pass
    return text


def create_file(text):
    selected_ex = get_extension(text)
    text = update_text(text)
    if "named" in text or "with name" in text:
        text = text.replace("named","")
        text = text.replace("with name","")
        text = text.replace("create","")
        text = text.strip()
        with open(f"{text}{selected_ex}","w"):
            pass
    else :
        with open(f"demo{selected_ex}","w"):
            pass



