function validate(){
    const username = document.getElementById("id_username").value;
    const f_name = document.getElementById("id_first_name").value;
    const l_name = document.getElementById("id_last_name").value;
    const email = document.getElementById("id_email").value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const password = document.getElementById("id_password").value;
    // const c_password = document.getElementById("c_password").value;
    var submition = 1;

    if(username == ""){
        document.getElementById("error_username").innerHTML = "Enter you're User name.";
        submition = 0;
    }

    else if(!isNaN(username) || (!isNaN(username[0]))){
        document.getElementById("error_username").innerHTML = "First latter must be alphabet."
        submition = 0;
    }

    else{
        document.getElementById("error_username").innerHTML = "";
        submition = 1;
    }

    if(f_name == ""){
        document.getElementById("error_f_name").innerHTML = "Enter you're First name.";
        submition = 0;
    }

    else if(!isNaN(f_name) || (!isNaN(f_name[0]))){
        document.getElementById("error_f_name").innerHTML = "First latter must be alphabet."
        submition = 0;
    }

    else{
        document.getElementById("error_f_name").innerHTML = "";
        submition = 1;
    }

    if(l_name == ""){
        document.getElementById("error_l_name").innerHTML = "Enter you're Last name.";
        submition = 0;
    }

    else if(!isNaN(l_name) || (!isNaN(l_name[0]))){
        document.getElementById("error_l_name").innerHTML = "First latter must be alphabet."
        submition = 0;
    }

    else{
        document.getElementById("error_l_name").innerHTML = "";
        submition = 1;
    }


    if(email == ""){
        document.getElementById("error_email").innerHTML = "Enter your Mail ID";
        submition = 0;

    }
    else if(!isNaN(email)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        submition = 0;

    }
    else if(validRegex.test(email)==false){
        document.getElementById("error_email").innerHTML = "Enter valid email.";
        submition = 0;
    }
    else{
        document.getElementById("error_email").innerHTML = "";
        submition = 1;
    }

    if(password == ""){
        document.getElementById("error_password").innerHTML = "Enter your password.";
        submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        submition = 0;
    }

    else{
        document.getElementById("error_password").innerHTML = "";
        submition = 1;
    }

    // if(c_password == ""){
    //     document.getElementById("error_c_password").innerHTML = "Confirm your password."
    //     submition = 0;
    // }

    // else if(password != c_password){
    //     document.getElementById("error_c_password").innerHTML = "Your password doesn't match."
    //     submition = 0;
    // }

    // else{
    //     document.getElementById("error_c_password").innerHTML = "";
    //     submition = 1;
    // }

    if(submition===1){
        // document.getElementById("submit").innerHTML = "Submited";
        return true;
    }
    else{
        return false;
    }
}

function login_validate(){
    const email = document.getElementById("id_email").value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    const password = document.getElementById("id_password").value;
    var submition = 1;

    if(email == ""){
        document.getElementById("error_email").innerHTML = "Enter your Mail ID";
        submition = 0;

    }
    else if(!isNaN(email)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        submition = 0;

    }
    else if(validRegex.test(email)==false){
        document.getElementById("error_email").innerHTML = "Enter valid email.";
        submition = 0;
    }
    else{
        document.getElementById("error_email").innerHTML = "";
        submition = 1;
    }

    if(password == ""){
        document.getElementById("error_password").innerHTML = "Enter your password.";
        submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        submition = 0;
    }

    else{
        document.getElementById("error_password").innerHTML = "";
        submition = 1;
    }

    if(submition===1){
        return true;
    }
    else{
        // document.getElementById('error_password').innerHTML = "Invalid Credentials."
        return false;
    }
}

function product_validate(){
    const product_name = document.getElementById("id_product_name").value;
    const product_disc = document.getElementById("id_product_discription").value;
    const product_img = document.getElementById("id_product_image").value;
    const product_price = document.getElementById("id_product_price").value;
    const product_category = document.getElementById("id_product_category").value;
    const quantity = document.getElementById("id_quantity").value;

    var submition = 1;

    if(product_name == ""){
        document.getElementById("error_product_name").innerHTML = "Enter Product name.";
        submition = 0;
    }
    else if(!isNaN(product_name)){
        document.getElementById("error_product_name").innerHTML = "Enter valid Product Name."
        submition = 0;
    }
    else{
        document.getElementById("error_product_name").innerHTML = "";
        submition = 1;
    }


    if(product_disc == ""){
        document.getElementById("error_product_disc").innerHTML = "Enter Product Dicription.";
        submition = 0;
    }
    else{
        document.getElementById("error_product_disc").innerHTML = "";
        submition = 1;
    }


    if(product_img == ""){
        document.getElementById("error_product_img").innerHTML = "Upload a Product Image.";
        submition = 0;
    }
    else{
        document.getElementById("error_product_img").innerHTML = "";
        submition = 1;
    }

    if(product_price == ""){
        document.getElementById("error_product_price").innerHTML = "Enter Product Price.";
        submition = 0;
    }
    else if(isNaN(product_price) || product_price < 1){
        document.getElementById("error_product_price").innerHTML = "Enter a valid product price."
        submition = 0;
    }
    else{
        document.getElementById("error_product_price").innerHTML = "";
        submition = 1;
    }

    if(product_category == ""){
        document.getElementById("error_product_category").innerHTML = "Select Product Category.";
        submition = 0;
    }
    else{
        document.getElementById("error_product_category").innerHTML = "";
        submition = 1;
    }

    if(quantity == ""){
        document.getElementById("error_quantity").innerHTML = "Enter Product Quantity.";
        submition = 0;
    }
    else if(isNaN(quantity)){
        document.getElementById("error_quantity").innerHTML = "Enter a valid product quantity."
        submition = 0;
    }
    else{
        document.getElementById("error_quantity").innerHTML = "";
        submition = 1;
    }


    if(submition===1){
        return true;
    }
    else{
        return false;
    }
}