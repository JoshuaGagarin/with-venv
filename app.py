from flask import Flask, render_template, request, jsonify
import numpy as np
import time

chat_data = (  #(data[0])
    {
  "hi": [
    "hi",
    "hey",
    "hola",
    "ahoy",
    "yo"
  ],
  "hello": [
    "hello",
    "hola"
  ],
  "goodbye": [
    "bye",
    "goodbye",
    "byegood"
  ],
  "return-policy": [
    "policy",
    "return",
    "policy-return"
  ],
  "return": [
    "return",
    "returning",
    "item",
    "refund",
    "exchange"
  ],
  "store-hours": [
    "hours",
    "hours-store",
    "time",
    "open",
    "open-store",
    "Opening",
    "opening-store",
    "Closing",
    "closing-store",
    "Schedule",
    "schedule-store",
    "Operation"
  ],
  "order-tracking": [
    "order-track",
    "track",
    "Status",
    "Transit",
    "package"
  ],
  "payment-method": [
    "payment",
    "method",
    "paying",
    "mode",
    "pay",
    "Cash",
    "Card",
    "Debit",
    "Bank"
  ],
  "size-guide": [
    "sizing",
    "sizing-find",
    "size",
    "size-find",
    "sizes",
    "guide",
    "measurement",
    "measurement-find",
    "measurements",
    "measurements-find",
    "Fit",
    "chart",
    "dimensions",
    "height",
    "width"
  ],
  "shipping-cost": [
    "much-delivery",
    "much-rate",
    "much-shipping",
    "shipping-cost",
    "rate",
    "charge",
    "fee",
    
  ],
  "discount-codes": [
    "discount-available",
    "discount",
    "discounts-available",
    "discounts",
    "codes",
    "promotions",
    "promotions-available",
    "promo-available",
    "promo",
    "promos",
    "promotion-available",
    "promotion",
    "offer",
    "offers",
    "sales-available",
    "sales",
    "sale-available",
    "sale",
  ],
  "store-location": [
    "location",
    "location-store",
    "located",
    "located-store",
    "physical",
    "physical-store",
    "address",
    "find"
  ],
  "customer-support": [
    "contact",
    "customer",
    "support",
    "number",
    "person",
    "assistance",
    "service",
    "helpdesk",
    "hotline"
  ],
  "thank-you": [
    "thank",
    "thank-help",
    "thanks",
    "thanks-help"
  ],
  "delivery": [
    "delivery",
    "delivery-available",
    "deliver",
    "deliver-available",
    "shipment",
    "transport",
    "ship",
    "shipping",
    "shipping-available"
  ],
  "shipping-options": [
    "offer-shipping",
    "shipping-options",
    "delivery-options",
    "deliver-options",
    "shipment-options",
    "transport",
    "transport-options"
  ],
  "gift-wrapping": [
    "gift-wrappping",
    "wrap",
    "gift"
  ],
  "okay": [
    "okay"
  ],
  "help": [
    "help",
    "help-hi",
    "assist"
  ],
  "bored": [
    "bored",
    "boring"
  ],
  "product-care":[
    "maintain",
    "maintenance",
    "preserve",
    "product-care",
    "keep-condition",
    "take-care"
  ],
  "product-availablity":[
    "product-availability",
    "available"
  ],
  "order-change":[
    "order-change"
  ],
  "shoes": [
    "shoes"
  ],
  "create-account":[
    "create-account",
    "signup",
    "sign-up"
  ],
  "sold-products":[
    "sell",
    "available-products",
    "available",
    "products"  
  ]
}
) 

response_dict =  ( # (response[0])
{
  "hi": "Hello there!",
  "hello": "Hi there!",
  "goodbye": "Bye see you later",
  "return-policy": "Our return policy allows you to return items within 30 days of purchase. Items must be unworn, unwashed, and in their original condition with tags attached.",
  "return": "To return an item, you can visit our returns page [link to returns page]. You'll need your order number and the email address used for the purchase. Follow the instructions provided, and you'll receive a return label to send the item back to us.",
  "store-hours": "We are open from 8am to 5pm, Monday to Friday",
  "order-tracking": "You can track your order using the tracking number provided in your order confirmation email. Simply enter the tracking number on our tracking page, and you'll see the latest updates on your shipment.",
  "payment-method": "We accept Visa, MasterCard, American Express, and PayPal. Additionally, you can use store credit or gift cards for your purchases.",
  "size-guide": "You can find our size guide on each product page, just below the product description. It provides measurements for each size to help you find the perfect fit.",
  "product-care": "Always wash similar colors together in cold water, use mild detergent, and avoid bleach. For drying, air dry flat or tumble dry on low heat. When storing, fold items neatly to maintain their shape, and store in a cool, dry place away from direct sunlight.",
  "shipping-cost": "Shipping costs vary based on your location and the shipping method you choose. Standard shipping is free for orders over $50. For detailed shipping rates, please visit our shipping information page.",
  "discount-codes": "We often have promotions and discount codes available. Please check our promotions page or subscribe to our newsletter to receive the latest discounts and offers.",
  "store-location": "We have several physical stores across the country. You can find the nearest store to your location by using the store locator on our website.",
  "product-availablity": "For information regarding product availability, please refer to the live view of the item and consult the indicated stock quantity displayed below the product.",
  "customer-support": "You can reach our customer support team via email at support@clothingstore.com or call us at 1-800-123-4567. Our support hours are Monday to Friday, 9 AM to 6 PM.",
  "thank-you": "You're welcome! If you have any other questions or need further assistance, feel free to ask.",
  "delivery": "Yes, we do offer shipping. For more details on shipping options, costs, and delivery times, please visit our Shipping Information page or contact our support team.",
  "okay": "Great! If there's anything you'd like to talk about or any questions you have, feel free to let me know. I'm here to help!",
  "help": "Of course! What do you need help with?",
  "how-are-you": "I'm just a chatbot, so I don't have feelings, but I'm here and ready to help you!",
  "bored": "How about read a book, watch a movie, go for a walk, or try out a new hobby?",
  "shipping-options": "We offer standard, expedited, and overnight shipping. Standard shipping usually takes 5-7 business days, expedited takes 2-3 business days, and overnight shipping delivers by the next business day.",
  "gift-wrapping":"Yes, we offer gift wrapping for an additional fee. You can select the gift wrapping option at checkout.",
  "sold-products": "We sell a wide range of fashionable clothing and accessories for men and women. Our collection includes trendy tops, stylish dresses, comfortable casual wear, elegant formal attire, and a variety of unique accessories such as bags, shoes, jewelry, and hats.",
  "shoes": "Yes, we do! We have a wide variety of shoes for men, women, and children.",
  "order-change": "If you need to change your order, please contact our customer service team as soon as possible. We'll do our best to accommodate your request if the order hasn't been processed yet.",
  "create-account": "To create an account, click on the 'Sign Up' button at the top of our homepage and follow the instructions. You can also create an account during the checkout process."
}
)

# chat_list = [] moved below
# response_list = []
app = Flask(__name__)

training_dict = {}

for intent, question_list in chat_data.items(): #chat_data.items()
    
   for question in question_list:
     training_dict[question] = intent
 

# Separating Features i.e questions and Labels i.e intents
feature =np.array(list(training_dict.keys()))
labels = np.array(list(training_dict.values()))
feature, labels
# WordVecotr with TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
# Converting text to WordVector
tf_vec = TfidfVectorizer().fit(feature)
X = tf_vec.transform(feature).toarray()
# Reshaping labels to fit data
y = labels.reshape(-1)

# Classifier
from sklearn.ensemble import RandomForestClassifier
# Fitting model
rnn = RandomForestClassifier(n_estimators=200)
rnn.fit(X, y)

chat_list = []
response_list = []
# chat_leest = ["Honda", "yamaha", "suzuki", "kawasaki", "Toyota","Mitsubishi"] 
# response_leest = ["Civic", "nmax", "GSX-r", "ninja400", "vios", "mirage"]

def botanswer(q):
    process_text = tf_vec.transform([q]).toarray()
    prob = rnn.predict_proba(process_text)[0]
    max_ = np.argmax(prob)

    if prob[max_] <= 0.6: #Only 60% and above accurate
        response_list.append("Sorry, I don't have much information about your query...")
        # return "Sorry I am not getting you...!"         turned this off
    else:
        response_list.append(response_dict[rnn.classes_[max_]])
        return response_dict[rnn.classes_[max_]]


  

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        chat_list.append(task)
        botanswer(task)
    return jsonify({'status': 'success'})

@app.route("/")
def home():
    print(chat_list)
    print(response_list)
    # return render_template('index.html',todos=chat_leest, responses=response_leest, zip=zip)
    return render_template('index.html',todos=chat_list, responses=response_list, zip=zip)

if __name__ == '__main__':
  app.run(debug=True)