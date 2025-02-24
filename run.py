from deal.app import ProductInfo
from deal.avaliablility_handler import CheckAvailability
from deal.price_handler import HandlePrice
from deal.mail_notification import ConfirmationMail
from deal.db import DatabaseHandler

datahandler= DatabaseHandler()
productinfo = ProductInfo()
productinfo.search_product()
info_dict = productinfo.get_product()

mail= input("enter the mail you want to receive notifications on: ")
choice = int(input("Enter: \n1. if you want to set up notifications for availability of the product \n2. if you want to set up notifications for a discount on your product"))

if(choice==1):
    ca = CheckAvailability(info_dict["link"], info_dict["shoesize"])
    dataset = ca.check_availability()
    ca.close_driver()
    datahandler.store_availability_request(mail,dataset["link"], dataset["name"], info_dict["shoesize"])
    cm = ConfirmationMail(mail)
    cm.send_confirmation()
    print("your request has been submitted! You'll Receive a confirmation Mail of the same.")
if(choice==2):
    thprice= int(input("Enter the price(prices lower than this price will be notified): "))
    hp= HandlePrice(thprice, info_dict["link"], info_dict["shoesize"])
    dataset = hp.check_price()
    hp.closedriver()
    datahandler.store_price_request(mail, info_dict["link"], dataset["name"], dataset["price"], info_dict["shoesize"])
    cm = ConfirmationMail(mail)
    cm.send_confirmation()
    print("your request has been submitted! You'll Receive a confirmation Mail of the same.")