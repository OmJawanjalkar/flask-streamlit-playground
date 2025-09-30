## put and Delete-HTTP VERBS
## Working with REST APIs--JSON data

from flask import Flask, jsonify, request

app = Flask(__name__)

##   Intial data in my do do list
items = [
  {"id":1, "name": "Iteam1", "description": "This is item 1"},
  {"id":2, "name": "Iteam2", "description": "This is item 2"}
]


@app.route('/')
def home():
    return "Welcome to the TO-DO-LIST API"

## Get: Retrieve all the items

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

#get: Retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"})
    return jsonify(item)


## Post: Create a new task -- ApI
@app.route('/items', methods=['POST'])
def create_item():
  if not request.json or 'name' not in request.json:
    return jsonify({"error": "item is not found"})

  new_item = {
    "id": items[-1]['id'] + 1 if items else 1,   # Auto-increment ID
    "name": request.json['name'],                # Required field
    "description": request.json.get('description', "")  # Optional field
}

  items.append(new_item)
  return jsonify(new_item)

## put: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
  item = next((item for item in items if item['id'] == item_id), None)
  if item is None:
      return jsonify({"error": "Item not found"})
  item['name'] = request.json.get('name', item['name'])
  item['description'] = request.json.get('description', item['description'])
  return jsonify(item)

## Delete: Remove an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
  global items
  items = [item for item in items if item['id'] != item_id]
  return jsonify({"result": "Item deleted"})






if __name__ == "__main__":
    app.run(debug=True)