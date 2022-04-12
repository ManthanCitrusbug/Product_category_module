$(document).ready(function () {
    $("#searchbtn").click(function (event) {
        event.preventDefault()
        const search = $("#searchinput").val()
        let csrf = $("input[name=csrfmiddlewaretoken]").val()
        $.ajax({
            url: 'search',
            method: 'GET',
            data: {'search': search, 'csrfmiddlewaretoken':csrf},
            success: function (data) {
                let search_data = data.data
                console.log(search_data)
                if(search.length > 0){
                    $('.hide').hide()
                    $('.paginater-hide').hide()
                    $.each(search_data, function(key, val){
                        console.log(val.name)
                        $(".main").append(`
                        <div class="jumbotron m-5 mt-5 main">
                        <img src="${val.image}" class="image_container" alt="" width="250px" height="250px"> 
                        <h1 class="display-4" id="product_name">${val.name}</h1> 
                        <p class="lead">${val.discription}</p>
                        <hr class="my-4">
                        <p>₹${val.price}</p>
                        <p>${val.category}</p>
                        <p>Quantity : ${val.quantity}</p>
                        <p>${val.user}</p>
                        <a class="btn btn-primary btn-lg" href="/details/${val.id}" role="button">Details</a>  
                        <form action="/add-to-cart/${val.id}" method="POST" class="d-inline mx-1">
                        <input type="hidden" name="csrfmiddlewaretoken" value=${csrf}>
                        <button class="btn btn-warning btn-lg">Add to cart</button>
                        </form>
                        <form action="/add-to-wish-list/${val.id}" method="POST" class="d-inline mx-1">
                        <input type="hidden" name="csrfmiddlewaretoken" value=${csrf}>
                        <button class="btn btn-info btn-lg">Add to wish list</button>
                        </form>
                        </div>
                        `)     
                    });
                }    
            }
        });
    });
});



$(document).ready(function(){
    $(".plus").click(function(event){
        event.preventDefault()
        let x = this.parentNode.children[1].innerText
        let z = parseInt(x);
        y = z+1
        this.parentNode.children[1].innerText = ""
        this.parentNode.children[1].innerText = y   
    });
});



$(document).ready(function(){
    $(".minus").click(function(event){
        event.preventDefault()
        let x = this.parentNode.children[1].innerText
        let z = parseInt(x);
        if(z>0){
            y = z-1
        }else{
            y=0
        }
        this.parentNode.children[1].innerText = ""
        this.parentNode.children[1].innerText = y   
    });
});

let price = $('.price').attr('pid').val()
console.log(price);
