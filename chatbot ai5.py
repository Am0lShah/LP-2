import re

def chatbot_response(user_input):
    user_input = user_input.lower()
    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to our grocery store. How can I help you today?",
        r"\b(2|how are you)\b": "I'm just a bot, but I'm here to assist you with groceries!",
        r"\b(3|order status|track order)\b": "Please provide your order ID to check the status.",
        r"\b(4|shipping time|delivery time)\b": "We offer same-day delivery and standard shipping (3-5 business days).",
        r"\b(5|return policy)\b": "You can return items within 7 days if unopened. Would you like help with a return?",
        r"\b(6|thank you|thanks)\b": "You're welcome! Let me know if you need anything else.",
        r"\b(7|price|cost)\b": "Please specify the product name to check its price.",
        r"\b(8|milk)\b": "Milk is 30rs per liter.",
        r"\b(9|eggs)\b": "A dozen eggs cost 80rs.",
        r"\b(10|rice)\b": "Rice is 50rs per kg.",
        r"\b(11|vegetables|veggies)\b": "We have fresh vegetables available. What are you looking for?",
        r"\b(12|fruits)\b": "We have apples, bananas, and oranges in stock. Which one do you need?",
        r"\b(13|snacks)\b": "We have chips, biscuits, and chocolates available.",
        r"\b(14|beverages|drinks)\b": "We have soft drinks, juices, and bottled water. What would you like?",
        r"\b(15|buy|order)\b": "You can place an order on our website or visit our store.",
        r"\b(16|payment methods)\b": "We accept cash, credit/debit cards, and UPI payments.",
        r"\b(17|store hours|timing)\b": "Our store is open from 8 AM to 10 PM every day.",
        r"\b(18|location|address)\b": "We are located at XYZ Market, Main Street, City.",
        r"\b(19|bye|exit)\b": "Goodbye! Happy shopping! 🛍"
    }
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific grocery item?"

# Chatbot interaction loop
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")
while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Happy shopping! 🛍")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)

'''Here’s a **complete explanation** of the Python chatbot code you provided, along with sample **input-output behavior** and **key concepts** used:

---

## 🧠 **Purpose of the Code**

This is a **basic rule-based chatbot** implemented in Python using **regex (regular expressions)** to respond to grocery-related queries.

---

## ⚙️ How the Code Works

### 1. **Importing the Module**

```python
import re
```

* `re` module is used to **match patterns** in user input via **regular expressions**.

---

### 2. **chatbot\_response() Function**

This function takes `user_input`, normalizes it to lowercase, and checks it against pre-defined regex patterns.

```python
def chatbot_response(user_input):
    user_input = user_input.lower()
    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to our grocery store. How can I help you today?",
        ...
        r"\b(19|bye|exit)\b": "Goodbye! Happy shopping! 🛍"
    }
```

* `\b` stands for **word boundary**, so "hi" matches but "highlight" doesn’t.
* The keys are **regex patterns**, and the values are pre-defined **chatbot responses**.

The function loops through the dictionary:

```python
for pattern, response in responses.items():
    if re.search(pattern, user_input):
        return response
```

* It uses `re.search()` to find a match.
* Returns the corresponding response if a pattern matches.
* If nothing matches:

```python
return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific grocery item?"
```

---

### 3. **Main Interaction Loop**

```python
print("Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")
```

This loop keeps asking for user input and responds accordingly:

```python
while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Happy shopping! 🛍")
        break
```

* Breaks out if user says "bye" or "exit".
* Otherwise, passes input to `chatbot_response()` and prints the result.

---

## 📥 Example Input and Output

### 🧑 You: `Hi`

🤖 Chatbot: Hello! Welcome to our grocery store. How can I help you today?

### 🧑 You: `How are you`

🤖 Chatbot: I'm just a bot, but I'm here to assist you with groceries!

### 🧑 You: `What’s the price of eggs?`

🤖 Chatbot: A dozen eggs cost 80rs.

### 🧑 You: `What is your return policy?`

🤖 Chatbot: You can return items within 7 days if unopened. Would you like help with a return?

### 🧑 You: `exit`

🤖 Chatbot: Goodbye! Happy shopping! 🛍

---

## 🧩 Concepts Used

| Concept             | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| `re.search()`       | Finds the first location where the regex pattern produces a match |
| `\b` in regex       | Word boundary, to ensure exact word match                         |
| Dictionary Matching | A simple way to map questions to responses                        |
| `input()`           | To interact with the user                                         |
| `while True:`       | Loop to keep the chatbot running                                  |
| Case Normalization  | Converts input to lowercase to make matching more robust          |

---

## ✅ Strengths

* Simple and easy to understand
* Can match both numbers (like "1") and phrases (like "hi")
* Covers a wide range of grocery-related FAQs

## ❌ Limitations

* Not intelligent; works only on exact or similar patterns
* Can't handle complex sentences like "Can you tell me how much rice costs?"

---

Would you like me to help you upgrade this chatbot using **Natural Language Processing (NLP)** or add **GUI support** (like Tkinter or web interface)?
'''