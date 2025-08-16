from django.shortcuts import render,HttpResponse,redirect
from .models import Inventory,Sales_Data,Contact,Bookings
import numpy  as np
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# password for login is parva_2565
def Home(request):
    # This function handles the home page, booking a table, and displaying a success message.
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
            name= request.POST.get("person_name")
            person_numbe=request.POST.get("person_number")
            population= request.POST.get("population")
            bookings=Bookings.objects.create(name=name,number=person_numbe,No_of_people=population,date=datetime.now())
            bookings.save()
            messages.success(request, "Your table has been booked. Have a good day !")
    return HttpResponse(render(request,'Home.html'))

def menu(request):
    # This function retrieves inventory data, handles item purchases, updates inventory, and redirects to the bill page.
    data = Inventory.objects.all().values()
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        quantity = request.POST.get("quantity")

        # Check if both item_id and quantity are provided
        if item_id and quantity:
            try:
                item_id = int(item_id)
                quantity = int(quantity)
            except ValueError:
                messages.error(request, "Please enter valid numbers for item and quantity.")
                return render(request, 'Menu.html', {"Data": data})

            item = Inventory.objects.get(id=item_id)
            if quantity <= item.quantity:
                total_price = item.price * quantity

                # Update Inventory
                item.quantity -= quantity
                item.save()

                # Store in Sales_Data
                Sales_Data.objects.create(
                    menu_items=item,
                    quantity_sold=quantity,
                    price=item.price,
                    Total_Price=total_price
                )

                return redirect('bill')  # Redirect to the bill page after order
            elif not item:
                messages.error(request, "Selected item does not exist.")
            elif quantity > item.quantity:
                messages.error(request, "Requested quantity exceeds available stock.")

    return render(request, 'Menu.html', {"Data": data})

def bill(request):
    # This function retrieves sales data and generates an invoice number for the bill page.
    main2 = Sales_Data.objects.select_related('menu_items').order_by('-id')
    invoice_No = np.random.choice(np.arange(1, 10), size=6)
    invoice_main = '-'.join(map(str, invoice_No))  # or use '-'.join(map(str, invoice_No)) for dash-separated
    grand_total = sum(item.Total_Price for item in main2)
    return render(request, 'Bill.html', {"main2": main2, "invoice_No": invoice_main , 'grand_total': grand_total})


def contact(request):
    # This function handles the contact form submission and displays a success message.
    if request.method=="POST":
        name=request.POST.get("name")
        Email=request.POST.get("Email")
        phone=request.POST.get("phone")
        State=request.POST.get("State")
        City=request.POST.get("City")
        message=request.POST.get("message")
        contact=Contact.objects.create(name=name,Email=Email,phone=phone,state=State,city=City,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent. We will get back to you soon.")
    return render(request, "contact_us.html")

def Loginuser(request):
    # This function authenticates a user and logs them in, redirecting to the home page upon success.
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
             
              messages.error(request, "Enter a valid username and password")
              return HttpResponse(render(request,"login.html"))
    return HttpResponse(render(request,"login.html"))

def Logoutuser(request):
    # This function logs out the current user and redirects them to the login page.
    logout(request)
    return redirect('/login')

# admin username=admin_12345
# password= admin_1234
# thanks for viewing the code