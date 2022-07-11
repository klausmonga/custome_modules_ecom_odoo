{
    "name": "Website Product Custom Description",
    "summary": """
        Add separate description field to website product view.
    """,
    "author": "Ahmed Mnasri",
    "website": "https://polyline.xyz",
    "category": "Ecommerce",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "depends": ["website_sale"],
    "data": [
        "views/product_product_normal_form_view.xml",
        "views/product_product_template_form_view.xml",
        "views/website_sale_product_template.xml",
    ],
    "installable": True,
    "application": False,
    "images": ["static/description/banner.png"],
}
