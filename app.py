from fastapi import FastAPI
myapp=FastAPI()
@myapp.get('/")
def homepage():
    return {
        "School":"Netligent IT Solutions",
        "Location":"Bhopal",
        "Message":"We are commited to build future"
    }
@myapp.get("/about")
def about_institute():
    return {
        "about":"Netligent IT solutions provide the quality and most demanding courses in IT industry"
    }
@myapp.get("/Courses")
def courses():
    return {
        "courses":[
            "Python",
            "Devops",
            "Network Architecture",
            "Cyber Secuiriy",
            "Data Analytics"
        ]
    }    
@myapp.get("/contac")
def contact():
    return {
        "address":"Building 4, 2nd Floor, Krishak nagar, karond, Bhopal"
    }
if __name__ == "__main__":
    uvicorn.run(myapp, host="0.0.0.0", port=8081)    
           
           

