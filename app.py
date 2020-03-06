from dashboard import app

if __name__ == "__main__":
    
    app.run(debug = True, threaded = True)
    #for multiple users set threaded = True
    #debug = true, allows the server to reload itself when changes are made