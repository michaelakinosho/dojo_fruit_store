from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

fruits_available = [{'name':'Apple','image_name':'apple.png'},{'name':'Blackberry','image_name':'blackberry.png'},{'name':'Raspberry','image_name':'raspberry.png'},{'name':'Strawberry','image_name':'strawberry.png'}]

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    order_detail = request.form
    ordered_fruits_info = fruits_list(order_detail)
    print(order_detail)
    print(ordered_fruits_info)
    return render_template("checkout.html",order_info = ordered_fruits_info)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html",fruits=fruits_available)

#Helper function to determine list of fruits
def fruits_list(order_dict):
    sum_fruits = 0
    list_of_fruits = list()
    fruit_orders = dict()
    user_info = dict()
    for fruit in fruits_available:
        list_of_fruits.append(fruit['name'])
        
    for k,v in order_dict.items():
        
        if k in list_of_fruits and v != '0':
                fruit_orders[k]= int(v)
                sum_fruits += int(v)
            
        else:
            user_info[k]=v
    return [fruit_orders,user_info,sum_fruits]

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! Page Not Available."

#@app.errorhandler(TypeError)
#def checkout_error(error):
#    return render_template("index.html")

if __name__=="__main__":   
    app.run(debug=True)