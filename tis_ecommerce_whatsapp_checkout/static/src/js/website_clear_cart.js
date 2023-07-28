odoo.define('website_clear_cart_whtsapp_chk.js', function (require) {
"use strict";
    console.log("entered");
    var ajax = require('web.ajax');
    $(function(){
    var oe_website_sale = this;
    $(oe_website_sale).on("click", ".whatsapp_checkout", function () {
        console.log("clicked");
        ajax.jsonRpc("/shop/clear_cart", "call", {}).then(function(){
            location.reload();
        });
    });
    });
    });
