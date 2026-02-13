products_schema = {
    "type": "object",
    "properties": {
        "products": {
            "type": "array"
        }
    },
    "required": ["products"]
}

login_schema = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "integer"},
        "message": {"type": "string"}
    },
    "required": ["responseCode", "message"]
}
