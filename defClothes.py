"""
defClothes.py defines 3 large categories of clothes, including suits, bottoms,
and tops. For each large category, their are more specified subcategories. There 
are 9 subcategories of clothes in total. And we will use these 9 subcategories as 
the target categories we are trying to classify the input data. These classification
are made by us which we think are natural and logical, and we think the ANN should be 
able to finish this classification task.
"""

# Suits
suits = ["suit"]

# Bottoms
shorts = ["shorts"]
bottoms = ["trousers", "trouser", "jeans", "pants", "sweatpants", "jogger", "chino"]

# Tops
shirts = ["shirt", "sportshirt"]
tops = ["sweater", "sweatshirt", "hoodie"]
jacket = ["jacket"]
blazers = ["blazer", "sportcoat", "coat"]
vests = ["vest"]
tshirts = ["t-shirt", "poloshirt"]

article_text = ["suit", "shorts", "bottoms", "shirt", "top", "jacket", "blazer", "vest", "tshirt"]
article_list = [suits, shorts, bottoms, shirts, tops, jacket, blazers, vests, tshirts]

h = 80
w = 60