#------------------------------
#Necessary Packages(Non-builtins)
#pyspellchecker
#------------------------------
from datetime import date
from spellchecker import SpellChecker
import re
current_day = date.today()
with open(f"merchant_questionaire_data_{current_day}", "r") as myfile:
    raw_text = myfile.read()
    myfile.close()
merchants_raw_text = raw_text.split("\n\n")
merchants = []
#List of Appstle Competitors
competitors = ["Recharge", "Skio", "Seal", "Loop", "Bold", "Recurpay", "Yotpo", "Bold", "Simplee", "Conjured", "Locksmith", "Inveterate", "Smile", "Lion", "Growave", "Rivo", "Joy"]
print("Good Morning,\nHere is your daily merchant digest:\n")

for merchant in merchants_raw_text:
    merchant_name = merchant[10:merchant.find("Which App(s) did you want to discuss for this meeting?:")].strip()
    #Start Apps needed Check
    apps_needed_raw_text = merchant[(merchant.find("Which App(s) did you want to discuss for this meeting?:")+56):merchant.find("Which Shopify Plan are you currently using?")]
    merchant_apps_needed = set()
    spell = SpellChecker()
    for word in apps_needed_raw_text.split():
        cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word).title()
        correction_possibilities = spell.candidates(cleaned_word)
        if "Subscriptions" in correction_possibilities or "Subscription" in correction_possibilities:
            merchant_apps_needed.add("Subscriptions")
        elif "Memberships" in correction_possibilities or "Membership" in correction_possibilities:
            merchant_apps_needed.add("Memberships")
        elif "Loyalty" in correction_possibilities or "Loyalties" in correction_possibilities:
            merchant_apps_needed.add("Loyalty")
        elif "Bundles" in correction_possibilities or "Bundle" in correction_possibilities:
            merchant_apps_needed.add("Bundles")
    #Start Competitor Apps Check
    merchant_number_competitors = 0
    competitors_raw_text = merchant[(merchant.find("Have you used a Subscriptions, Memberships, or Loyalty App before? If yes, please name which app(s).: ") + 102):merchant.find("Please share your store link(s). Preferably your MyShopify URL.:")]
    for competitor in competitors:
        merchant_number_competitors += competitors_raw_text.count(competitor)
    #Start link
    link_raw_text = merchant[(merchant.find(
        "Please share your store link(s). Preferably your MyShopify URL.:") + 65):merchant.find(
        "We would like to record this meeting for training purposes and for your reference. You can also request a copy of this recording for your own use. Do you consent to recording this demo meeting?:")]
    if link_raw_text.__contains__("{") and link_raw_text.__contains__("}"):
        link = link_raw_text.split("{")[1].split("}")[0]
    else:
        link = "None"
    #Priority Things
    if merchant_number_competitors >= 1:
        priority = 1
    elif len(merchant_apps_needed) > 2:
        priority = 2
    else:
        priority = 3
    #Apps needed as string
    print(merchant_name)
    print("Apps Needed:", ", ".join(merchant_apps_needed))
    print("Priority Level: ", priority)
    print("Store Link: ", link)
    print()
