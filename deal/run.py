from deal.app import ProductInfo
from deal.avaliablility_handler import CheckAvailability
from deal.price_handler import HandlePrice
from deal.mail_notification import ConfirmationMail

productinfo = ProductInfo()
productinfo.search_product()
info_dict = productinfo.get_product()

choice = int(input("Enter: \n1. if you want to set up notifications for availability of the product \n2. if you want to set up notifications for a discount on your product"))

if(choice==1):
    ca = CheckAvailability(info_dict["link"], info_dict["shoes"])
    dataset = ca.check_availability()
    ca.close_driver()
    mail= input("enter the mail you want to receive notifications on: ")
    cm = ConfirmationMail("stupefyingbuttons@gmail.com")
    cm.send_confirmation()
    #add to database
    print("your request has been submitted! You'll Receive a confirmation Mail of the same.")
if(choice==2):
    hp= HandlePrice(info_dict["price"], 2000, info_dict["link"], info_dict["shoes"])
    dataset = hp.check_price()
    hp.closedriver()
    cm = ConfirmationMail("stupefyingbuttons@gmail.com")
    cm.send_confirmation()
    print("your request has been submitted! You'll Receive a confirmation Mail of the same.")