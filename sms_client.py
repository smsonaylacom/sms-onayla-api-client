from sms_client import SmsOnayla

# Initialize with your API Key
api = SmsOnayla(api_key="YOUR_API_KEY_HERE")

# 1. Get Balance
balance = api.get_balance()
print(f"Current Balance: {balance}")

# 2. Order a Number (Service ID for WhatsApp: 12)
order = api.buy_number(service="whatsapp", country="uk")
print(f"Number Ordered: {order['phone_number']} (ID: {order['id']})")

# 3. Get The Code
# The system waits until the code arrives...
code = api.get_sms(order_id=order['id'])
print(f"Your Verification Code: {code}")
