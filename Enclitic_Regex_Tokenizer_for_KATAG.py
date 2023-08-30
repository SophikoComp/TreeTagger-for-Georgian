#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: UTF-8 -*-


# In[2]:


from nltk.tokenize import WordPunctTokenizer


# In[3]:


# Step 2: Tokenize a string on whitespace using the Python split() method
def whitespace_tokenize(text):
    return text.split()


# In[4]:


# Step 3: Tokenize a text into a sequence of alphabetic and non-alphabetic characters
def word_punct_tokenize(text):
    tokenizer = WordPunctTokenizer()
    return tokenizer.tokenize(text)


# In[19]:


# Step 4: Tokenize a string if it ends on the specified clitics
def clitic_tokenize(tokens, clitics, exceptions):
    clitic_tokens = []
    
    for token in tokens:
        if any(token.endswith(clitic) for clitic in clitics) and token not in exceptions:
            for clitic in clitics:
                if token.endswith(clitic) and token[:-len(clitic)] not in exceptions:
                    clitic_tokens.append(token[:-len(clitic)])
                    clitic_tokens.append(clitic)
                    break
            else:
                clitic_tokens.append(token)
        else:
            clitic_tokens.append(token)
    
    return clitic_tokens


# In[20]:


# Step 5: Load the text from a file
def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# In[21]:


# Example usage:
input_filename = 'C:\\Users\\sophi\\Desktop\\input.txt'
text = load_text(input_filename)


# In[22]:


# Tokenize using WhitespaceTokenizer and WordPunctTokenizer
whitespace_tokens = whitespace_tokenize(text)
word_punct_tokens = word_punct_tokenize(text)


# In[23]:


# Define clitics and exceptions
clitics = [
    "თან", "თვის", "გან", "დან", "დამი", "დმი", "ებრ", "ვით", "ზე", "თანავე", "კენ",
    "მდე", "ურთ", "ში"
]

exceptions = [
    "თანდათან", "ჯონათან", "ერთვის", "დაერთვის", "ყოველთვის", "მართვის", "თიბათვის",
    "ნებართვის", "დატვირთვის", "მიმართვის", "ჩართვის", "რადგან", "ყველგან", "ერთგან",
    "ზოგან", "მაგან", "რადგან", "სხვაგან", "სხედან", "აქედან", "თავიდან", "იქიდან",
    "საიდან", "მადამი", "ადამი", "ამსტერდამი", "ნოტერდამი", "საჭიროებისამებრ",
    "სურვილისამებრ", "შესაძლებლობისამებრ", "შეძლებისამებრ", "შეხედულებისამებრ",
    "ჩემებრ", "ჩვეულებისაებრ", "წესისამებრ", "წეს-ჩვეულებისამებრ",
    "გეტყვით", "გამგზავრებულიყავით", "გამიშვით", "გამოთქვით", "გამოსულიყავით",
    "გარკვევით", "გარკვეულიყავით", "გაუსვით", "დაგეწევით", "დავით", "დავმდგარიყავით",
    "დასვით", "ექცევით", "ეხვევით", "ვეწევით", "ვიტყვით", "ვყოფილიყავით", "ზევით",
    "ზურგშექცევით", "თავით", "თავშექცევით", "თვით", "თქვით", "იბნევით", "იტყვით",
    "იყავით", "მასავით", "მეტყვით", "მიირთვით", "მიკივით", "მიხედვით", "მოეშვით",
    "მოვქცეულიყავით", "შევერევით", "შემთხვევით", "გამილამაზე", "მზე", "სილამაზე",
    "სინაზე", "სიბრაზე", "ამასთანავე", "აქეთკენ", "გტკენ", "იქითკენ", "რეკენ",
    "აქამდე", "ბოლომდე", "გასცემდე", "გამომდე", "გავჩუმდე", "გადმომდე",
    "გადამდე", "გასცემდე", "ვსვამდე", "იქამდე", "მანამდე", "როდემდე", "სადამდე",
    "ხევსურთ", "ბინძურთ", "გიაურთ", "გსურთ", "მესვეურთ", "მსახურთ", "სურთ", "ქურთ",
    "ყოვლითურთ", "ყურთ", "შურთ", "შემხვდურთ", "ჰსურთ", "ბოდიში", "შიში", "კალოში"
]


# In[24]:


# Tokenize using the custom clitic tokenizer
clitic_tokens = clitic_tokenize(word_punct_tokens, clitics, exceptions)


# In[25]:


# Print the output
for token in clitic_tokens:
    print(token)


# In[ ]:




