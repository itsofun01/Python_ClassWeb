#!\xampp\htdocs\Python_ClassWeb\venv\Scripts\python.exe

import json
import requests
import cgi

form = cgi.FieldStorage()
inputPrice = form.getvalue('price')
inputSort = form.getvalue('sort')
print("Content-type:text/html; charset=utf-8\n")

url = "http://localhost/Python_ClassWeb/search_price/service_price.py"

send_parameter = {}
send_parameter["price"] = inputPrice
send_parameter["sort"] = inputSort

r = requests.get(url,params=send_parameter)

data = json.loads(r.content)

def lib():
    print("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/js/all.min.js" integrity="sha256-MAgcygDRahs+F/Nk5Vz387whB4kSK9NXlDN3w58LLq0=" crossorigin="anonymous"></script>""")

def nav():
    print("<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>")
    print("<a class='navbar-brand' href='#'>Python Web Class</a>")
    print(
        "<button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarNav' aria-controls='navbarNav' aria-expanded='false' aria-label='Toggle navigation'>")
    print("<span class='navbar-toggler-icon'></span>")
    print("</button>")
    print("<div class='collapse navbar-collapse' id='navbarNav'>")
    print("<ul class='navbar-nav'>")
    print("<li class='nav-item'>")
    print("<a class='nav-link' href='http://localhost/Python_ClassWeb/basicmysql.py'>Home <span class='sr-only'>(current)</span></a>")
    print("</li>")
    print("<li class='nav-item'>")
    print("<a class='nav-link' href='http://localhost/Python_ClassWeb/insert.py'>Add Product</a>")
    print("</li>")
    print("<li class='nav-item'>")
    print("<a class='nav-link' href='http://localhost/Python_ClassWeb/CUID.py'>Customer Management</a>")
    print("</li>")
    print("<li class='nav-item'>")
    print("<a class='nav-link' href='http://localhost/Python_ClassWeb/request1.py'>Service</a>")
    print("</li>")
    print("<li class='nav-item active'>")
    print("<a class='nav-link' href='http://localhost/Python_ClassWeb/search_price/request_price.py'>Price</a>")
    print("</li>")
    print("</ul>")
    print("</div>")
    print("</nav><br>")

def query():
    if(data == 'no'):
        print("<div class='col-4 card' style='margin-bottom: 10px;'>No data</div>")
    else:
        for i in data:
            print("<div class='col-4 card' style='margin-bottom: 10px;'>")
            print("<div class='card-header'>")
            print("<span class='badge badge-info'>ID&nbsp;#{}</span>".format(i['id']))
            print("</div>")
            print("<div class='card-body'>")
            print("<b>Name:</b> {}<br>".format(i['name']))
            print("<b>Price:</b> {}".format(i['price']))
            print("</div>")
            print("</div>")

print("<html>")
print("<head>")
lib()
print("</head>")
print("<body>")
nav()
print("<div class='container'>")
print("""<form class='form-group' action="request_price.py" method="POST">
        <div class='row'>
            <div class='col-12' align='center'>
                <h1>Search Product Price</h1>
            </div>
            <div class='col-12 row margin-10' style='justify-content: center;' >
                <div class='col-3'>
                    <input type='text' class='form-control' name='price' placeholder='Enter Product Price'>
                </div>
                <div class='col-12 row' align='center' style='justify-content: center;'>
                    <div class="form-check" style='margin-right: 10px;'>
                      <input class="form-check-input" type="radio" name="sort" id="exampleRadios1" value="1" checked>
                      <label class="form-check-label" for="exampleRadios1">
                        ASC
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="sort" id="exampleRadios2" value="2">
                      <label class="form-check-label" for="exampleRadios2">
                        DESC
                      </label>
                    </div>
                </div>
                <div class='col-12' align='center' style="margin-top: 10px;">
                <input type='submit' class='btn btn-info' value='Search'>
                <input type='submit' class='btn btn-warning' value='Reset'>
                </div>
            </div>
            
        </div>
    </form>""")
print("<div class='row'>")
query()
print("</div>")
print("</div>")
print("</body>")
print("</html>")
